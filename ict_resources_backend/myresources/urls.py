from django.urls import include, path
from rest_framework import routers

from myresources.views.CourseView import *
from myresources.views.ClasseView import *
from myresources.views.ScheduleView import *
# from myresources.views.ReservationScheduleView import *
from myresources.views.EquipmentView import *
from myresources.views.DepartmentView import *
from myresources.views.ReservationView import *
from myresources.views.NotificationsView import *

router = routers.DefaultRouter()

router.register(r'resources', ScheduleViewset)

router.register(r'equipment', EquipmentViewset)
router.register(r'reservationschedule', ReservationViewset)
router.register(r'notifications', NotificationsViewset)

urlpatterns = [

    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('getCategoryClasse/', CategoryClassView.as_view()),
    path('getClasseCategoryId/<int:pk>/', CategoryClasseGetId.as_view()),
    path('getClasse/', ClasseView.as_view()),
    path('getDepartmentFilierLevelId/<int:pk>/', getDepartmentFilierLevelId.as_view()),
    path('getAllDepartment/', getAllDepartment.as_view()),
    path('TypeScheduleView/', TypeScheduleView.as_view()),
    path('getCategorieNotification/', CategorieNotificationView.as_view()),

    # course

    path('getCourse/', GetCourse.as_view()),
    path('getCategoryCourse/', GetCategoryCourse.as_view()),

    ##reservation

]
