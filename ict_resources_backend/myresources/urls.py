from django.urls import include, path
from rest_framework import routers
from myresources.views.views import *

from myresources.views.views import *
from myresources.views.viewsets import *
router = routers.DefaultRouter()

router.register(r'resources', ScheduleViewset)





urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('user/all/', MeListView.as_view(), name="user-list"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path("all-profiles/", UserProfileListCreateView.as_view(), name="all-profiles"),
    # retrieves profile details of the currently logged in user
    path("profile/<int:pk>/", userProfileDetailView.as_view(), name="profile"),
    path("blacklist/", LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist'),


]

