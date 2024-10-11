from django.contrib import admin
from django.urls import path,include
from .views import AppointmentListCreateView,NewsAndEventDetailView,SingleBlog,DoctorsListCreateView,NewsAndEventListCreateView,BlogListCreateView,TestimonialListCreateView


urlpatterns = [
    path('appointments',AppointmentListCreateView.as_view(),name='appointment'),
    path('doctors',DoctorsListCreateView.as_view(),name='Doctors'),
    path('blogs',BlogListCreateView.as_view(),name='blogs'),
    path('blogs/<str:slug>',SingleBlog.as_view(),name='blog-detail'),
    path('news-events',NewsAndEventListCreateView.as_view(),name='news-events'),
    path('news-events/<str:slug>',NewsAndEventDetailView.as_view(),name='news-events-detial'),
    path('testimonials',TestimonialListCreateView.as_view(),name='testimonials'),
]