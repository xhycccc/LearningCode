from rest_framework import serializers
from .models import Course, CourseDetail

class CourseSerializers(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ('pk', 'CourseName', 'Cid')

class CourseDetailSerializers(serializers.ModelSerializer):
	class Meta:
		model = CourseDetail
		fields = ('pk', 'Cid', 'title', 'summary')