from django.db import models
from django.db.models import Max
from django.utils.text import slugify
from django.utils.translation import gettext as _
from django.db.models.signals import pre_save
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from utilities.models import AbstractBaseFields, Language
from customauth.models import User


class Category(AbstractBaseFields):
    parent = models.ForeignKey(
        'self', related_name='children', on_delete=models.CASCADE,
        blank=True, null=True
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(
        allow_unicode=True, unique=True, db_index=True, null=True,
        blank=True
    )
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='categories/')

    class Meta:
        """
        enforcing that there can not be two categories under a parent with same
        slug
        """
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])


class Course(AbstractBaseFields):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advance', 'Advance'),
    ]
    OVERVIEW_CHOICES = [
        ('youtube', 'YouTube'),
        ('vimeo', 'Vimeo'),
        ('html5', 'Html5'),
    ]
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        allow_unicode=True, unique=True, db_index=True, null=True,
        blank=True
    )
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    level = models.CharField(max_length=100, choices=LEVEL_CHOICES, null=True)
    language = models.ForeignKey(
        Language, on_delete=models.SET_NULL, null=True
    )
    is_top_course = models.BooleanField(
        _('Check if this is a top course'), default=False
    )
    is_free_course = models.BooleanField(
        _('Check if this is a free course'), default=False
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_has_discount = models.BooleanField(
        _('Check if this course is a has discount'), default=False
    )
    discount_percentage = models.IntegerField(
        help_text="The Discount range is 0 to 100.",
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    course_overview_provider = models.CharField(
        max_length=100, choices=OVERVIEW_CHOICES
    )
    course_overview_url = models.URLField(max_length=255)
    course_thumbnail = models.ImageField(upload_to='course/')
    meta_keywords = models.CharField(max_length=255)
    meta_description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Requirement(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course.title} {self.title}"


class Outcome(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course.title} {self.title}"


class Section(AbstractBaseFields):
    course = models.ForeignKey(
        Course, on_delete=models.PROTECT, related_name='sections'
    )
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Lesson(AbstractBaseFields):
    TYPE_CHOICES = [
        ('youtube', 'Youtube'),
        ('vimeo', 'Vimeo'),
        ('html5', 'HTML5'),
        ('video_file', 'Video File'),
        ('google_drive', 'Google Drive'),
        ('document', 'Document'),
        ('image_file', 'Image File'),
        ('iframe_embed', 'Iframe Embed'),
    ]
    section = models.ForeignKey(
        Section, on_delete=models.PROTECT, related_name='section_lessions'
    )
    title = models.CharField(max_length=255)
    course = models.ForeignKey(
        Course, on_delete=models.PROTECT, related_name='lessons'
    )
    provider = models.CharField(
        max_length=30, choices=TYPE_CHOICES, default='youtube'
    )
    video_url = models.URLField(null=True, blank=True)
    file = models.FileField(upload_to='lessons/', null=True, blank=True)
    duration = models.CharField(max_length=255)
    summary = models.TextField()
    order = models.PositiveIntegerField()
    is_free = models.BooleanField(
        "Make as free lesson",
        help_text="Do you want to keep it free as a preview video?",
        default=False
    )

    def __str__(self):
        return self.title


class Enrollment(AbstractBaseFields):
    """ Enrollment """
    student = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='student_enrollments'
    )
    course = models.ForeignKey(
        Course, on_delete=models.PROTECT, related_name='course_enrollments'
    )

    def __str__(self):
        return f"{self.student.email} - {self.course.title}"


def payment_number():
    """ Payment number """
    invoice_id = Payment.objects.aggregate(max_inv=Max('number'))['max_inv']
    if invoice_id is not None:
        return invoice_id + 1
    return 0


class Payment(AbstractBaseFields):
    """ payment model (Instructor) """
    number = models.PositiveIntegerField(
        default=payment_number, db_index=True, unique=True, null=True,
        editable=False
    )
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='user_payments'
    )
    course = models.ForeignKey(
        Course, on_delete=models.PROTECT, related_name='course_payments'
    )
    payment_type = models.CharField(max_length=100)
    phone = models.CharField(
        _('Mobile Phone'), max_length=12, blank=True, null=True,
        validators=[RegexValidator(  # min: 10, max: 12 characters
            r'^[\d]{10,12}$', message='Format (ex: 0123456789)'
        )]
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.email} {self.course.title} {self.amount}"


# functions
def unique_slug_generator(instance):
    """ unique_slug_generator """
    constant_slug = slugify(instance.title)
    slug = constant_slug
    num = 0
    Klass = instance.__class__
    while Klass.objects.filter(slug=slug).exists():
        num += 1
        slug = "{slug}-{num}".format(slug=constant_slug, num=num)
    return slug


# course slug generate
def pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug or instance.title != Course.objects.filter(
        slug=instance.slug
    ):
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_reciever, sender=Course)
