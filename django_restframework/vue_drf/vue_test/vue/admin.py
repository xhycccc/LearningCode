from django.contrib import admin
from .models import Course, CourseDetail
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk','CourseName', 'Cid')

@admin.register(CourseDetail)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display = ('pk','Cid','title', 'summary')