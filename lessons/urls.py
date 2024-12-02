from django.urls import path

from . import views

urlpatterns = [
    path("<int:number>/", views.detail,name="lesson_detail"),
    path("<int:number>/responder/", views.responder_leccion,name="lesson_respond"),
    path("<int:number>/terminar/", views.terminar_leccion,name="lesson_respond"),
    path('list/', views.list, name='lessons_list'),
]