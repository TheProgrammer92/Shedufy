from django.urls import include, path
from rest_framework import routers

from myresources.views.viewsets import *
from myresources.views.views import *

router = routers.DefaultRouter()

router.register(r'resources', ScheduleViewset)

router.register(r'equipment', EquipmentViewset)
router.register(r'reservationSchedule', ReservationScheduleViewset)

urlpatterns = [

    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('getCategoryClasse/', CategoryClassView.as_view()),
    path('getClasseCategoryId/<int:pk>/', CategoryClasseGetId.as_view()),
    path('getClasse/', ClasseView.as_view()),

    #course

    path('getCourse/', GetCourse.as_view()),
    path('getCategoryCourse/', GetCategoryCourse.as_view()),

    ##reservation


]
