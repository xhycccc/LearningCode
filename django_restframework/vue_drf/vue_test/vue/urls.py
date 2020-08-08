from django.conf.urls import include, url
from rest_framework import routers
from vue import views

route = routers.DefaultRouter()
route.register(r'course', views.CourseSet)
route.register(r'course_detail', views.CourseDetailSet)
urlpatterns = [
    url('api/', include(route.urls))
]