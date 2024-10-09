from django.contrib import admin
from.models import Appointment,Doctor,HealthMetric,Blog,NewsAndEvents,Testimonial,Prescription

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Doctor)
admin.site.register(HealthMetric)
admin.site.register(Blog)
admin.site.register(NewsAndEvents)
admin.site.register(Testimonial)
admin.site.register(Prescription)
