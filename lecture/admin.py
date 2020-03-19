from django.contrib import admin
from .models import Lecture

# Register your models here.

class LectureAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'lecturer')

admin.site.register(Lecture, LectureAdmin)
