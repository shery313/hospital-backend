from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from .serializers import AppointmentSerializer,DocterSerializer
from .models import Appointment,Docter

# Create your views here.
class AppointmentListCreateView(ListCreateAPIView):
    queryset=Appointment.objects.all()
    serializer_class=AppointmentSerializer
    permission_classes=[AllowAny,]
class DoctersListCreateView(ListCreateAPIView):
    queryset=Docter.objects.all()
    serializer_class=DocterSerializer
    permission_classes=[AllowAny,]