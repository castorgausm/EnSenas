from django.contrib import admin

from lessons.models import Lesson, LessonImage

admin.site.register(Lesson)
admin.site.register(LessonImage)