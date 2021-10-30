# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Social


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
