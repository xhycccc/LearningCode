from django.db import models

# Create your models here.
class Course(models.Model):
    CourseName = models.CharField('CoueseName', max_length=100, default='noname')
    Cid =  models.CharField('Cid', max_length=100, default='noname')

class CourseDetail(models.Model):
    Cid = models.CharField('Cid', max_length=100)
    title = models.CharField('title', max_length=100, default='[notitle]')
    summary = models.CharField('summary', max_length=200, default='')
