from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	usertype = models.CharField(max_length=30)
	gender=models.CharField(max_length=10)
	address=models.CharField(max_length=200)
	age=models.IntegerField()
	rollno=models.IntegerField()

class Subject(models.Model):
	name=models.CharField(max_length=30)


class Results(models.Model):
	student=models.ForeignKey(User, on_delete=models.DO_NOTHING)
	subject=models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
	marks=models.CharField(max_length=10)
	total=models.CharField(max_length=10)


		