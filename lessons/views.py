from django.http import Http404
from django.shortcuts import render
from lessons.models import Lesson, LessonImage


def detail(request, number):
    try:
        l = Lesson.objects.get(number=number)
    except Lesson.DoesNotExist:
        raise Http404("Lesson does not exist")
    
    lesson_images = LessonImage.objects.filter(lesson=l)

    return render(request, "lesson.html", {"lesson": l, "lesson_images": lesson_images})