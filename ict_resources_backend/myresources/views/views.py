from django.core.paginator import Paginator
from django.shortcuts import render

from rest_framework import status, permissions

from rest_framework.generics import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from myresources.models import *
from myresources.serializer import *
from myresources.views.viewsets import ScheduleViewset
from myresources_profil.serializer import *

# Create your views here.

from django.contrib.auth import get_user_model

User = get_user_model()


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page'
    max_page_size = 1000


class ClasseView(ListAPIView):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)

        return Response({'data': serializer.data})


class CategoryClassView(ListAPIView):
    serializer_class = CategoryClassSerializer
    queryset = CategoryClasse.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        tab_classe = []
        for category in queryset:
            classe = category.classe.all()

            tab_classe.append(classe)

        serializer_classe = ClasseSerializer(tab_classe, many=True)
        serializer = self.get_serializer(queryset, many=True)

        return Response({'data': serializer.data})


class CategoryClasseGetId(ListAPIView):
    serializer_class = CategoryClassSerializer
    queryset = CategoryClasse.objects.all()

    def get(self, request, pk=None, *args, **kwargs):
        queryset = CategoryClasse.objects.get(pk=pk)
        tab_classe = queryset.classe.all()

        serializer_classe = ClasseSerializer(tab_classe, many=True)

        return Response({'data': serializer_classe.data})


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
