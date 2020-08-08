from rest_framework import viewsets, filters, pagination
from .models import Student
from .serializers import StudentSerializers

class PageSet(pagination.PageNumberPagination):
	page_size = 3
	page_size_query_param = 'size'
	max_page_size = 10
	page_query_param = 'page'

class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all().order_by('-pk')

	serializer_class = StudentSerializers
	pagination_class = PageSet
	filter_backends = (filters.SearchFilter,)
	search_fields = ('=name', 'id')
	ordering_field = ('name','sid')