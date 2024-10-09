from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from .serializers import AppointmentSerializer,DoctorSerializer,BlogSerializer,TestimonialSerializer,NewsAndEventSerializer
from .models import Appointment,Doctor,Blog,Testimonial,NewsAndEvents

# Create your views here.
class AppointmentListCreateView(ListCreateAPIView):
    queryset=Appointment.objects.all()
    serializer_class=AppointmentSerializer
    permission_classes=[AllowAny,]
class DoctorsListCreateView(ListCreateAPIView):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer
    permission_classes=[AllowAny,]
class BlogListCreateView(ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    permission_classes=[AllowAny,]
class TestimonialListCreateView(ListCreateAPIView):
    queryset=Testimonial.objects.all()
    serializer_class=TestimonialSerializer
    permission_classes=[AllowAny,]
class NewsAndEventListCreateView(ListCreateAPIView):
    queryset=Testimonial.objects.all()
    serializer_class=NewsAndEventSerializer
    permission_classes=[AllowAny,]