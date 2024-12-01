

from django.contrib.auth.models import User
from lessons.models import Lesson,LessonUser

def inscribir_usuario(user:User):
    lessons = Lesson.objects.all()
    print(lessons)

    for lesson in lessons:
        LessonUser.objects.create(lesson=lesson, user=user)


