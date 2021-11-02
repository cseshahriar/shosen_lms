# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Category, Course, Requirement, Outcome, Enrollment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_user',
        'updated_user',
        'is_active',
        'created',
        'updated',
        'parent',
        'title',
        'slug',
        'description',
        'image',
    )
    list_filter = (
        'created_user',
        'updated_user',
        'is_active',
        'created',
        'updated',
        'parent',
    )
    search_fields = ('slug',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_user',
        'updated_user',
        'is_active',
        'created',
        'updated',
        'title',
        'slug',
        'short_description',
        'description',
        'category',
        'level',
        'language',
        'is_top_course',
        'is_free_course',
        'price',
        'is_has_discount',
        'discount_percentage',
        'course_overview_provider',
        'course_overview_url',
        'course_thumbnail',
        'meta_keywords',
        'meta_description',
    )
    list_filter = (
        'created_user',
        'updated_user',
        'is_active',
        'created',
        'updated',
        'category',
        'language',
        'is_top_course',
        'is_free_course',
        'is_has_discount',
    )
    search_fields = ('slug',)


@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'title')
    list_filter = ('course',)


@admin.register(Outcome)
class OutcomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'title')
    list_filter = ('course',)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_user',
        'updated_user',
        'is_active',
        'created',
        'updated',
        'student',
        'course',
    )
    list_filter = (
        'created_user',
        'updated_user',
        'is_active',
        'created',
        'updated',
        'student',
        'course',
    )
