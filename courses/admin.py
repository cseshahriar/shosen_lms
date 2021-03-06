# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import (
    Category, Course, Requirement, Outcome, Enrollment, Section, Lesson,
    Payment, Comment, Rating
)


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


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_user',
        'updated_user',
        'is_active',
        'created',
        'updated',
        'course',
        'title',
        'code',
    )
    list_filter = (
        'created_user',
        'updated_user',
        'is_active',
        'created',
        'updated',
        'course',
    )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_user',
        'updated_user',
        'is_active',
        'created',
        'updated',
        'section',
        'title',
        'course',
        'provider',
        'video_url',
        'file',
        'duration',
        'summary',
        'order',
        'is_free',
    )
    list_filter = (
        'created_user',
        'updated_user',
        'is_active',
        'created',
        'updated',
        'section',
        'course',
        'is_free',
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_user',
        'updated_user',
        'is_active',
        'created',
        'updated',
        'number',
        'user',
        'course',
        'payment_type',
        'phone',
        'amount',
        'is_paid',
    )
    list_filter = (
        'created_user',
        'updated_user',
        'is_active',
        'created',
        'updated',
        'user',
        'course',
        'is_paid',
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'body',
        'user',
        'content_type',
        'object_id',
        'is_active',
        'created',
        'updated',
    )
    list_filter = ('user', 'content_type', 'is_active', 'created', 'updated')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'student',
        'review',
        'rating',
        'content_type',
        'object_id',
        'is_active',
        'created',
        'updated',
    )
    list_filter = (
        'student',
        'content_type',
        'is_active',
        'created',
        'updated',
    )
