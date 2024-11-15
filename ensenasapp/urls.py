from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.start_view, name='start'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('lesson/', views.lesson_view, name='lesson'),
    path('profile/', views.profile_view, name='profile'), 
    path('lessons/', views.lessons_view, name='lessons'),
    path("lecciones/", include("lessons.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


