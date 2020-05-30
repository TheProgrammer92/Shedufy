from django.urls import include, path
from rest_framework import routers
from myresources.views.views import *

from myresources.views.views import *
from myresources.views.viewsets import *
from myresources.views.viewsets_users import *
router = routers.DefaultRouter()

router.register(r'resources', ScheduleViewset)
router.register(r'user', UserViewset)
router.register(r'classe', ClasseViewset)
router.register(r'equipment', EquipmentViewset)





urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('classe/', include('djoser.urls.jwt')),
    path('user/all/', MeListView.as_view(), name="user-list"),

    path("blacklist/", LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist'),


]

