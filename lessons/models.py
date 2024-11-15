from django.db import models

class LessonImage(models.Model):
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    position = models.IntegerField()

class Lesson(models.Model):
    number = models.IntegerField(unique=True)
    question = models.CharField(max_length=200)
    response = models.CharField(max_length=200, null=True)
    
