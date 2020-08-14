
from rest_framework.generics import *

from rest_framework.response import Response


from myresources.serializer import *

# Create your views here.

from django.contrib.auth import get_user_model

from myresources.views.ClasseView import StandardResultsSetPagination

User = get_user_model()



class GetCourse(ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)
        return Response({'data': serializer.data})


class GetCategoryCourse(ListAPIView):
    serializer_class = CategoryCourseSerializer
    queryset = CategoryCourse.objects.all()
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)
        return Response({'data': serializer.data})
