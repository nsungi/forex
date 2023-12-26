from django.contrib import admin
from .models import (ImageUpload, TextUpload, Course, Technical, 
                     Fundamental, Risk, Analysis, Trick, Pschology, Pair)

# Register your models here.

class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'date_uploaded',)
    search_fields = ['user__username', 'description']

class TextUploadAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_uploaded',)
    search_fields = ['user__username']

class CourseAdmin(admin.ModelAdmin):
    list_display = ('user', 'title',)
    search_fields = ['user__username', 'title']

class TechnicalAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'date_uploaded',)
    search_fields = ['user__username', 'title__title']

class FundamentalAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'date_uploaded',)
    search_fields = ['user__username', 'title__title']

class RiskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'date_uploaded',)
    search_fields = ['user__username', 'title__title']

class AnalysisAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'date_uploaded',)
    search_fields = ['user__username', 'title__title']

class TrickAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'date_uploaded',)
    search_fields = ['user__username', 'title__title']

class PschologyAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'date_uploaded',)
    search_fields = ['user__username', 'title__title']

class PairAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'date_uploaded',)
    search_fields = ['user__username', 'title__title']

# Register your models with the custom ModelAdmin classes
admin.site.register(ImageUpload, ImageUploadAdmin)
admin.site.register(TextUpload, TextUploadAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Technical, TechnicalAdmin)
admin.site.register(Fundamental, FundamentalAdmin)
admin.site.register(Risk, RiskAdmin)
admin.site.register(Analysis, AnalysisAdmin)
admin.site.register(Trick, TrickAdmin)
admin.site.register(Pschology, PschologyAdmin)
admin.site.register(Pair, PairAdmin)
