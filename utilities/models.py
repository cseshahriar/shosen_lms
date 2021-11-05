import logging

# DJANGO IMPORTS
from django.db import models
from django.conf import settings
from customauth.models import User
from django.core.cache import cache
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import RegexValidator

logger = logging.getLogger(__name__)


class AbstractBaseFields(models.Model):
    """ abstract base models """
    created_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="%(app_label)s_%(class)s_createdby"
    )
    updated_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="%(app_label)s_%(class)s_updated"
    )
    is_active = models.BooleanField(
        _('Is Active'), default=False
    )
    created = models.DateTimeField(
        _('Created At'), auto_now_add=True, null=True
    )
    updated = models.DateTimeField(
        _('Last Updated'), auto_now=True, null=True
    )

    def make_deactive(self):
        self.is_active = False
        self.save()

    def make_active(self):
        self.is_active = True
        self.save()

    class Meta:
        abstract = True


class Social(models.Model):
    PLATFORM_CHGOICES = [
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('github', 'Github')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(
        max_length=100, choices=PLATFORM_CHGOICES, null=True
    )
    url = models.URLField(max_length=100)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} {self.platform}"


class Language(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Coupon(models.Model):
    """ Coupon model """
    coupon_code = models.CharField(max_length=100)
    discount_percentage = models.IntegerField(
        help_text="The Discount range is 0 to 100.",
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    starting_date = models.DateTimeField(null=True, blank=True)
    expire_date = models.DateTimeField()

    def __str__(self):
        return self.coupon_code


class Currency(models.Model):
    """ Currency model """
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=100, unique=True)
    symbol = models.ImageField(upload_to='currencies/')
    paypal_supported = models.BooleanField(default=True)
    stripe_supported = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class FrontendSetting(models.Model):
    """ Frontend settings """
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='frontends/', null=True, blank=True)

    def __str__(self):
        return self.key


class Application(models.Model):
    """ leave applications """
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='applications'
    )
    document = models.FileField(upload_to='applications/')
    message = models.TextField()
    is_aproved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.detail[0:30])


class Message(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sender'
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='receiver'
    )
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sender} - {self.receiver}"


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)
        self.set_cache()

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)


class SiteSettings(SingletonModel):
    """
    References
    https://steelkiwi.com/blog/practical-application-singleton-design-pattern
    """
    website_name = models.CharField(max_length=255, default='Shosen LMS')
    website_title = models.CharField(
        max_length=255, default='Shosen Learning Management'
    )
    website_meta_key = models.CharField(
        max_length=255, help_text='Please add comma separated values'
    )
    website_meta_description = models.TextField()
    author = models.CharField(max_length=255, default='Author name')
    slogan = models.CharField(max_length=255, default='Slogan')
    info_email = models.EmailField(default='info@example.com')
    sales_email = models.EmailField(default='sales@example.com')
    support_email = models.EmailField(default='support@example.com')
    address = RichTextField()
    phone = models.CharField(
        _('Mobile Phone'), max_length=14, blank=True, null=True,
        validators=[RegexValidator(  # min: 10, max: 12 characters
            r'^(?:\+?88)?01[15-9]\d{8}$', message='Format (ex: 01234567890)'
        )]
    )
    youtube_api_key = models.CharField(
        max_length=255, default='ACbcad883c9c3e9d9913a715557dddff99'
    )
    vimeo_api_key = models.CharField(
        max_length=255, default='ACbcad883c9c3e9d9913a715557dddff99'
    )
    purchase_code = models.CharField(max_length=255, default='ABC001')
    system_language = models.ForeignKey(
        Language, on_delete=models.CASCADE, default=1, related_name='languages'
    )
    student_email_verification = models.BooleanField(default=False)
    footer_text = RichTextField(null=True)
    footer_link = models.CharField(max_length=255, null=True)
    twilio_account_sid = models.CharField(
        max_length=255, default='ACbcad883c9c3e9d9913a715557dddff99'
    )
    twilio_auth_token = models.CharField(
        max_length=255, default='abd4d45dd57dd79b86dd51df2e2a6cd5'
    )
    twilio_phone_number = models.CharField(
        max_length=255, default='+15006660005'
    )
    cookies_status = models.BooleanField(default=False)
    cookie_note = models.CharField(
        max_length=255,
        default="""This website uses cookie to personalize content and analyse
         in order to offer you a better exprerience."""
    )
    facebook = models.URLField(default='www.facebook.com/lsm')
    twitter = models.URLField(default='www.twitter.com/lsm')
    linkedin = models.URLField(default='www.linkedin.com/lsm')
    cookie_policy = RichTextField(null=True)
    about_us = RichTextField(null=True)
    terms_and_conditions = RichTextField(null=True)
    refound_policy = RichTextField(null=True)
    recaptcha_settings = models.BooleanField(default=False)
    recaptcha_sitekey = models.CharField(max_length=255, null=True, blank=True)
    recaptcha_secretkey = models.CharField(
        max_length=255, null=True, blank=True
    )
    recaptcha_version = models.IntegerField(
        default=2,
        validators=[
            MaxValueValidator(3),
            MinValueValidator(2)
        ]
    )
    banner = models.ImageField(
        upload_to='banner/', null=True,
        help_text='Upload banner image(2000x1335)px'
    )
    light_logo = models.ImageField(
        upload_to='logos/', null=True,
        help_text='Upload light logo(330x70)px'
    )
    dark_logo = models.ImageField(
        upload_to='logos/', null=True,
        help_text='Upload dark logo(330x70)px'
    )
    small_logo = models.ImageField(
        upload_to='logos/', null=True,
        help_text='Upload dark logo(49x58)px'
    )
    favicon = models.ImageField(
        upload_to='logos/', null=True,
        help_text='Upload dark logo(90x90)px'
    )
