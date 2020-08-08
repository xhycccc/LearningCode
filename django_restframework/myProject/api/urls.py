from django.conf.urls import include, url
from rest_framework import routers
from api import views

route = routers.DefaultRouter()
route.register(r'student', views.StudentViewSet)

urlpatterns = [
	url('api/', include(route.urls)),
]