from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from profile_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename= 'helloviewset') 
router.register('profile', views.UserProfileViewSet),
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()), 
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)) # genereaza o lista de urls asociate pt viewset

]

