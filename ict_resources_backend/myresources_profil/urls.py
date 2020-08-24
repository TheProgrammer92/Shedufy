from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from myresources_profil.views import *
from myresources_profil.viewsets import UserViewset

router = routers.DefaultRouter()
router.register(r'user', UserViewset)

urlpatterns = [


    path("blacklist/", LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist'),
    path("users/update_personnal_info", UserUpdatePersonnalInfoView.as_view()),
    path("users/update_avatar", AvatarUpdateView.as_view()),
    path("users/getAllUser", GetAllUser.as_view()),
    path("profil/create/", CreateUserView.as_view()),
    path('profil/verify_code/<slug:code>/', VerifyCodeView.as_view()),
    url('^social/', include('social_django.urls'))


]
