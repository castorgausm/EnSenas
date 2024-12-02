from django.db import models

class Lesson(models.Model):
    # Define los campos del modelo Lesson aquí
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Otros campos...

class Video(models.Model):
    # Define los campos del modelo Video aquí
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=200)
    # Otros campos...