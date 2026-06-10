from django.db import models
from cloudinary.models import CloudinaryField

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Student(models.Model):
    roll = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    profile_pic = CloudinaryField(
        'image',
        blank=True,
        null=True
    )
    age = models.IntegerField()
    dept = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )
    courses = models.ManyToManyField(Course)
    def __str__(self):
        return self.name