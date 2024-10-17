from django.contrib import admin
from django.urls import path,include
from .views import ContactListCreateView,NewsLetterListCreateView,AppointmentListCreateView,DoctorDetialView,NewsAndEventDetailView,SingleBlog,DoctorsListCreateView,NewsAndEventListCreateView,BlogListCreateView,TestimonialListCreateView


urlpatterns = [
    path('appointments',AppointmentListCreateView.as_view(),name='appointment'),
    path('doctors',DoctorsListCreateView.as_view(),name='Doctors'),
    path('doctors/<str:slug>',DoctorDetialView.as_view(),name='Doctors-detial'),
    path('blogs',BlogListCreateView.as_view(),name='blogs'),
    path('blogs/<str:slug>',SingleBlog.as_view(),name='blog-detail'),
    path('news-events',NewsAndEventListCreateView.as_view(),name='news-events'),
    path('news-events/<str:slug>',NewsAndEventDetailView.as_view(),name='news-events-detial'),
    path('testimonials',TestimonialListCreateView.as_view(),name='testimonials'),
    path('contact',ContactListCreateView.as_view(),name='contact'),
    path('news-letter',NewsLetterListCreateView.as_view(),name='news-letter'),
]