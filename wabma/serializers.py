from rest_framework.serializers import ModelSerializer
# from serializers import model
from .models import Appointment,Docter

class AppointmentSerializer(ModelSerializer):
    class Meta:
        model=Appointment
        fields='__all__'
class DocterSerializer(ModelSerializer):
    class Meta:
        model=Docter
        fields='__all__'
