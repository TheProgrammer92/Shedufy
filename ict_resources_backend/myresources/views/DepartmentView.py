from rest_framework.generics import *

from rest_framework.response import Response

from myresources.serializer import *

# Create your views here.

from django.contrib.auth import get_user_model

from myresources.views.ClasseView import StandardResultsSetPagination
from myresources_profil.serializer import UserSerialiser

User = get_user_model()


class getAllDepartment(ListAPIView):
    serializer_class = DepartmentListSerializer

    def list(self, request, *args, **kwargs):
        queryset_depart = Department.objects.all()
        serializer_depart = DepartmentListSerializer(queryset_depart, many=True)

        return Response({'data': serializer_depart.data})


class getDepartmentFilierLevelId(RetrieveAPIView):
    serializer_class = DepartmentListSerializer

    def retrieve(self, request, pk=None, *args, **kwargs):
        user = User.objects.get(pk=pk)
        profiles = user.profile.all().values()
        queryset_depart = None

        is_id_admin = self.request.GET.get('is_id_admin')

        queryset_depart = None

        if is_id_admin == "admin":
            for profile in profiles:
                queryset_depart = Department.objects.filter(pk=1)
        if is_id_admin == "guest":
            queryset_depart = Department.objects.filter(pk=1)
        # recherchons les departement

        depart_serializer = DepartmentListSerializer(queryset_depart, many=True)

        # recherchons les filieres liés a ces departement

        queryset_filiere = []
        tab_filiere = []
        for department in depart_serializer.data:
            queryset_filiere = Filiere.objects.filter(pk=department['id'])
            serializer_filiere = FiliereSerializer(queryset_filiere, many=True)
            tab_filiere.append(serializer_filiere.data[0])

        # recherchons les niveau en liée aux filiere
        tab_level = []
        for filiere in tab_filiere:
            for level in filiere['id_level']:
                queryset_level = Level.objects.filter(pk=level)
                serializer_level = LevelSerializer(queryset_level, many=True)
                tab_level.append(serializer_level.data[0])

        # Recherchons les cours liée au niveau
        tab_course = []
        for level in tab_level:

            for course in level['course']:
                queryset_course = Course.objects.filter(pk=course)
                serializer_course = CourseSerializer(queryset_course, many=True)
                tab_course.append(serializer_course.data[0])

        # les type d'evenement pour avoir les couleur

        # chargement des professeur
        queryset_teacher = User.objects.filter(is_teacher=True)
        serializer_teacher = UserSerialiser(queryset_teacher, many=True)

        return Response(
            {"department": depart_serializer.data, "filiere": tab_filiere, "level": tab_level, 'course': tab_course,
             'teacher': serializer_teacher.data})
