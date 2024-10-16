from rest_framework.serializers import ModelSerializer
# from serializers import model
from .models import Appointment,Doctor,NewsAndEvents,Testimonial,Blog,Newsletter,Contact

class AppointmentSerializer(ModelSerializer):
    class Meta:
        model=Appointment
        fields='__all__'
class DoctorSerializer(ModelSerializer):
    class Meta:
        model=Doctor
        fields='__all__'
class BlogSerializer(ModelSerializer):
    class Meta:
        model=Blog
        fields='__all__'
class NewsAndEventSerializer(ModelSerializer):
    class Meta:
        model=NewsAndEvents
        fields='__all__'
class TestimonialSerializer(ModelSerializer):
    class Meta:
        model=Testimonial
        fields='__all__'
class NewsLetterSerializer(ModelSerializer):
    class Meta:
        model=Newsletter
        fields='__all__'
class ContactSerializer(ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'
