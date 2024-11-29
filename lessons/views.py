from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lessons.models import Lesson, LessonImage,LessonUser

@login_required
def detail(request, number):
    # user = 
    try:
        lesson = Lesson.objects.get(number=number)
    except Lesson.DoesNotExist:
        raise Http404("Lesson does not exist")
    
    lesson_images = LessonImage.objects.filter(lesson=lesson)

    return render(request, f"lesson_{lesson.number}.html", {"lesson": lesson, "lesson_images": lesson_images})

@login_required
def list(request):

    user = request.user
    # print(user.first_name)
    lessons = LessonUser.objects.filter(user=user).order_by('lesson__number')
    # print(lessons)
    
    return render(request, "lessons.html", {"lessons": lessons})

@login_required
def responder_leccion(request,number):
    pass
