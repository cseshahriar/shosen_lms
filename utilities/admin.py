# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import (
    Social, Language, Coupon, Currency, Application,
    Message, SiteSettings, PaymentSettings, SMTPSettings, SocialSettings
)


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'platform',
        'url',
        'is_active',
        'created',
        'updated',
    )
    list_filter = ('user', 'is_active', 'created', 'updated')


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'coupon_code',
        'discount_percentage',
        'starting_date',
        'expire_date',
    )
    list_filter = ('starting_date', 'expire_date')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'document', 'message', 'is_aproved')
    list_filter = ('user', 'is_aproved')


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'currency',
        'code',
        'symbol',
        'paypal_supported',
        'stripe_supported',
    )
    list_filter = ('paypal_supported', 'stripe_supported')
    search_fields = ('name',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sender',
        'receiver',
        'message',
        'created',
        'updated',
    )
    list_filter = ('sender', 'receiver', 'created', 'updated')


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display_links = ('website_name',)
    list_display = (
        'id',
        'website_name',
        'website_title',
        'website_meta_key',
        'website_meta_description',
        'author',
        'slogan',
        'info_email',
        'sales_email',
        'support_email',
        'address',
        'phone',
        'youtube_api_key',
        'vimeo_api_key',
        'purchase_code',
        'system_language',
        'student_email_verification',
        'footer_text',
        'footer_link',
        'twilio_account_sid',
        'twilio_auth_token',
        'twilio_phone_number',
        'cookies_status',
        'cookie_note',
        'facebook',
        'twitter',
        'linkedin',
        'cookie_policy',
        'about_us',
        'terms_and_conditions',
        'refound_policy',
        'recaptcha_settings',
        'recaptcha_sitekey',
        'recaptcha_secretkey',
        'recaptcha_version',
        'banner',
        'light_logo',
        'dark_logo',
        'small_logo',
        'favicon',
    )
    list_filter = (
        'system_language',
        'student_email_verification',
        'cookies_status',
        'recaptcha_settings',
    )


@admin.register(PaymentSettings)
class PaymentSettingsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'active',
        'mode',
        'currency',
        'sandbox_client_id',
        'sandbox_secret_key',
        'production_client_id',
        'production_secret_key',
    )
    list_filter = ('active', 'currency')


@admin.register(SMTPSettings)
class SMTPSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'protocol', 'host', 'port', 'password')


@admin.register(SocialSettings)
class SocialSettingsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'facebook_active',
        'facebook_api_id',
        'facebook_api_secret',
        'youtube_active',
        'youtube_api_key',
        'youtube_restrict_key',
        'twitter_active',
        'twitter_api_key',
        'twitter_restrict_key',
        'vimeo_active',
        'vimeo_api_key',
        'vimeo_restrict_key',
    )
    list_filter = (
        'facebook_active',
        'youtube_active',
        'twitter_active',
        'vimeo_active',
    )
