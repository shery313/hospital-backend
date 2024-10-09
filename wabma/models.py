from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Complex real-world appointment model
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
    ]
    
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name='appointments')
    date = models.DateTimeField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    symptoms = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    # booking_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.patient.username} - {self.doctor.name} on {self.date}"


# Complex Doctor model with relationships and validation
class Doctor(models.Model):
    SPECIALTY_CHOICES = [
        ('Cardiology', 'Cardiology'),
        ('Neurology', 'Neurology'),
        ('Orthopedics', 'Orthopedics'),
        ('Pediatrics', 'Pediatrics'),
        ('Oncology', 'Oncology'),
        ('General', 'General Medicine'),
        # Add more specialties as needed
    ]
    
    name = models.CharField(max_length=200)
    image = models.ImageField(default='doctor.jpg', upload_to='media/doctors')
    specialty = models.CharField(max_length=100, choices=SPECIALTY_CHOICES)
    experience_years = models.PositiveIntegerField()
    bio = models.TextField()
    education = models.CharField(max_length=500, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    availability = models.BooleanField(default=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    schedule = models.JSONField(null=True, blank=True)  # Example: {'Monday': '9AM-5PM', 'Tuesday': '11AM-4PM'}

    class Meta:
        ordering = ['-rating']

    def __str__(self):
        return f"Dr. {self.name} ({self.specialty})"


# Blog model with more metadata
class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    published_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    featured_image = models.ImageField(upload_to='media/blogs', null=True, blank=True)

    def __str__(self):
        return self.title


# Complex Testimonial model with timestamp and approval process
class Testimonial(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='media/testimonials')
    name = models.CharField(max_length=200)
    message = models.TextField()
    approved = models.BooleanField(default=False)  # Requires admin approval
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (Approved: {self.approved})"


# News and Events model with multiple options
class NewsAndEvents(models.Model):
    CATEGORY_CHOICES = [
        ('News', 'News'),
        ('Event', 'Event'),
        ('Announcement', 'Announcement'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=15,default='News', choices=CATEGORY_CHOICES)
    event_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.title} - {self.category}"


# Prescription management related model
class Prescription(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='prescriptions')
    medication_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    prescribed_date = models.DateTimeField(auto_now_add=True)
    refill_status = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.medication_name} for {self.patient.username}"


# Health metric tracking for patients
class HealthMetric(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='health_metrics')
    metric_type = models.CharField(max_length=100)  # Example: Weight, Blood Pressure, etc.
    value = models.DecimalField(max_digits=5, decimal_places=2)
    measured_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.metric_type}: {self.value} for {self.patient.username}"
