from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('register', views.RegisterView)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.CustomAuthToken.as_view()),
]
