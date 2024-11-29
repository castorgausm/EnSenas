from django.contrib import admin

from lessons.models import Lesson, LessonImage,LessonUser

admin.site.register(Lesson)
admin.site.register(LessonImage)
admin.site.register(LessonUser)