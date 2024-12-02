from django.db import models
from django.contrib.auth.models import User


class LessonImage(models.Model):
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    position = models.IntegerField()

class Lesson(models.Model):
    number = models.IntegerField(unique=True)
    question = models.CharField(max_length=200)
    response = models.CharField(max_length=200, null=True)


class LessonUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    finished = models.BooleanField(default=False)



    
