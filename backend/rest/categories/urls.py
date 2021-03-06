from django.urls import path, include
from .views import GenericAPIView, DetailsAPIView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', GenericAPIView.as_view()),
    path('<int:id>', DetailsAPIView.as_view())
]