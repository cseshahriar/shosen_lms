import logging

# DJANGO IMPORTS
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from customauth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

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
