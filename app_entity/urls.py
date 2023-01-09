from django.urls import path
from . import views


urlpatterns = [
    path('entities/', views.EntityList.as_view(), name='entities'),
    ]

