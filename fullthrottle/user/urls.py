from django.urls import path, include
from . import views
from . views import UserViewSet
from rest_framework import routers
 


router = routers.DefaultRouter()
router.register("", UserViewSet)
urlpatterns = [
    path('',views.user_list,name='user_list'),
    path("api/userview", include(router.urls))
    ]
