#coding=utf8
from django.db import models
import datetime
import django
# Create your models here.

class Test(models.Model):
    name=models.CharField(max_length=50,null=True)
    age=models.IntegerField(null=True)
    def __str__(self):
        return self.name


class Topic(models.Model):
    name=models.CharField(max_length=30)
    add_date=models.DateTimeField(null=True,auto_now=True)
    def __str__(self):
        return self.name

class Article(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    content=models.TextField()
    def __str__(self):
        return self.content[:20]