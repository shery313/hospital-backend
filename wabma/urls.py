from django.contrib import admin
from django.urls import path,include
from .views import AppointmentListCreateView,DoctersListCreateView


urlpatterns = [
    path('',AppointmentListCreateView.as_view(),name='appointment'),
    path('docters',DoctersListCreateView.as_view(),name='docters'),
]