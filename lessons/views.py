from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lessons.models import Lesson, LessonImage,LessonUser
from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



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

@csrf_exempt
@login_required
def responder_leccion(request,number):

    user = request.user
    try:
        lesson = LessonUser.objects.get(lesson__number=number,user=user)
    except Lesson.DoesNotExist:
        raise Http404("Lesson does not exist")
    
    data = json.loads(request.body)
    respuesta = data.get('respuesta')
    # respuesta = request.POST.get('respuesta')
    is_correct = respuesta.lower().strip() == lesson.lesson.response.lower().strip()

    if is_correct:
        lesson.finished = True
        lesson.save()


    return JsonResponse({
            'correct': is_correct,
    })

@csrf_exempt
@login_required
def terminar_leccion(request,number):

    user = request.user
    try:
        lesson = LessonUser.objects.get(lesson__number=number,user=user)
    except Lesson.DoesNotExist:
        raise Http404("Lesson does not exist")
    
    lesson.finished = True
    lesson.save()
    return HttpResponse("terminado", content_type='plain/txt')
    
    
    # if respuesta.lower() == lesson.lesson.response:
    #     lesson.finished = True
    #     lesson.save()
    #     print("Correcta")
    #     return HttpResponse("correct", content_type='plain/txt')
    # else: 
    #     print("Incorrecta")
    #     return HttpResponse("incorrect", content_type='plain/txt')



    






    
    




