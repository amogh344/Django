from django.db import models
class Student_info(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
