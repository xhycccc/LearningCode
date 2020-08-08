from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import CourseSerializers, CourseDetailSerializers
from .models import Course, CourseDetail


class LoginView(APIView):
    def get(self, request, *args, **kargs):
        ret = {
            'code': 111,
            'data': 'get method'
        }

        response = JsonResponse(ret)
        response['Access-Control-Allow-Origin']='*'
        return response

    def post(self, request, *args, **kwargs):
        print(request.body)
        print(request.POST)
        print('post')
        ret = {
            'code': 1000,
            'username': 'haiyn',
            'token': 'sdswr4fdfsdfdxqw2fgh',
        }
        response = JsonResponse(ret)
        response['Access-Control-Allow-Origin'] = "*"
        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers']='*'
        return response

class CourseView(APIView):
    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get('pk')
        if pk:
            print(kwargs.get('pk'))
            ret = {
                'title': 'titletitle',
                'summary': 'happy'
            }
        else:
            ret = {
                'code': 1000,
                'courseList':[
                    {'name': 'Frank', 'id':1},
                    {'name': 'Jack', 'id':2},
                    {'name': 'Fried', 'id': 3},
                ]
            }
        response = JsonResponse(ret)
        response['Access-Control-Allow-Origin'] = '*'
        return response

class CourseSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('pk')
    serializer_class = CourseSerializers

class CourseDetailSet(viewsets.ModelViewSet):
    queryset = CourseDetail.objects.all().order_by('pk')
    serializer_class = CourseDetailSerializers

