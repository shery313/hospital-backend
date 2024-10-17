from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import shortuuid


# Complex real-world appointment model
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
    ]
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name='appointments')
    name=models.CharField(max_length=300)
    email=models.EmailField()
    phone=models.IntegerField()
    date = models.DateTimeField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    # symptoms = models.TextField(null=True, blank=True)
    # status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    booking_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.email} - {self.doctor.name} on {self.date}"


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
    slug=models.SlugField(null=True,blank=True)

    class Meta:
        ordering = ['-rating']

    def __str__(self):
        return f"Dr. {self.name} ({self.specialty})"
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug is None:
            uuid_key = shortuuid.uuid()
            uniqueid = uuid_key[:4]
            self.slug = slugify(self.name) + "-" + str(uniqueid.lower())
        super(Doctor, self).save(*args, **kwargs)


# Blog model with more metadata
class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    published_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    featured_image = models.ImageField(upload_to='media/blogs', null=True, blank=True)
    slug=models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug is None:
            uuid_key = shortuuid.uuid()
            uniqueid = uuid_key[:4]
            self.slug = slugify(self.title) + "-" + str(uniqueid.lower())
        super(Blog, self).save(*args, **kwargs)

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
    image=models.FileField(upload_to='media/news-events',null=True,blank=True)
    category = models.CharField(max_length=15,default='News', choices=CATEGORY_CHOICES)
    event_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    slug=models.SlugField(null=True,blank=True)
    def __str__(self):
        return f"{self.title} - {self.category}"
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug is None:
            uuid_key = shortuuid.uuid()
            uniqueid = uuid_key[:4]
            self.slug = slugify(self.title) + "-" + str(uniqueid.lower())
        super(NewsAndEvents, self).save(*args, **kwargs)



class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.IntegerField()
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Newsletter(models.Model):
    email=models.EmailField(unique=True)
    is_subscribed=models.BooleanField(default=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
