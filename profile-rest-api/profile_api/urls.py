from django.urls import re_path, path, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from profile_api import views

router = DefaultRouter() 
router.register('register', views.UserProfileViewSet)



urlpatterns = [
     
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
     # genereaza o lista de urls asociate pt viewset
    path('messages/', views.MessageApiView.as_view()),

    ]

