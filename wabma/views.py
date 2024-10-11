from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView
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
class SingleBlog(RetrieveAPIView):
    serializer_class = BlogSerializer
    def get_object(self):
        # Retrieve the product using the provided slug from the URL
        slug = self.kwargs.get('slug')
        return Blog.objects.get(slug=slug)
class TestimonialListCreateView(ListCreateAPIView):
    queryset=Testimonial.objects.all()
    serializer_class=TestimonialSerializer
    permission_classes=[AllowAny,]
class NewsAndEventListCreateView(ListCreateAPIView):
    queryset=NewsAndEvents.objects.all()
    serializer_class=NewsAndEventSerializer
    permission_classes=[AllowAny,]
class NewsAndEventDetailView(RetrieveAPIView):
    serializer_class=NewsAndEventSerializer
    def get_object(self):
        slug=self.kwargs.get('slug')
        return NewsAndEvents.objects.get(slug=slug)