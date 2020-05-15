from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
from .views import UserProfileListCreateView, userProfileDetailView, LogoutAndBlacklistRefreshTokenForUserView


urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path("all-profiles/", UserProfileListCreateView.as_view(), name="all-profiles"),
    # retrieves profile details of the currently logged in user
    path("profile/<int:pk>/", userProfileDetailView.as_view(), name="profile"),
    path("blacklist/", LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist')

]