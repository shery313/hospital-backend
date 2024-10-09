from django.contrib import admin
from django.urls import path,include
from .views import AppointmentListCreateView,DoctorsListCreateView,NewsAndEventListCreateView,BlogListCreateView,TestimonialListCreateView


urlpatterns = [
    path('',AppointmentListCreateView.as_view(),name='appointment'),
    path('Doctors',DoctorsListCreateView.as_view(),name='Doctors'),
    path('blogs',BlogListCreateView.as_view(),name='blogs'),
    path('news-events',NewsAndEventListCreateView.as_view(),name='news-events'),
    path('testimonials',TestimonialListCreateView.as_view(),name='testimonials'),
]