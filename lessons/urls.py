from django.urls import path

from . import views

urlpatterns = [
    path("<int:number>/", views.detail,name="lesson_detail"),
    path('list/', views.list, name='lessons_list'),
]