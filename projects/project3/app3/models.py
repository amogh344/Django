from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

class TaskBoard(models.Model):
    task_name=models.CharField(max_length=100)
    task_description=models.TextField()