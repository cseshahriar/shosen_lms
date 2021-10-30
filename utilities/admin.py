# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Social, Language


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
