from django.core.exceptions import ValidationError
from django.db import models
from django.utils.deconstruct import deconstructible

class PersonalInfo(models.Model):
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    contact_phone = models.CharField(max_length=15)
    contact_email = models.EmailField()
    nationality = models.CharField(max_length=20)
    profile_thumbnail = models.ImageField(upload_to='profile_thumbnails/', null=True, blank=True)
    linkedin_profile = models.URLField(null=True, blank=True)
    github_profile = models.URLField(null=True, blank=True)
    x_profile = models.URLField(null=True, blank=True)
    insta_profile = models.URLField(null=True, blank=True)
    fb_profile = models.URLField(null=True, blank=True)
    whatsApp_profile = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.full_name

class About(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title

class Language(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='language_icons/', null=True, blank=True)
    percentage = models.IntegerField(default=0, help_text='Proficiency percentage')

    def __str__(self):
        return self.title
    
@deconstructible
class SVGValidator:
    def __call__(self, value):
        if value.file.content_type != 'image/svg+xml':
            raise ValidationError('Only SVG files are allowed.')


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    pricing = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='service_images/', null=True, blank=True)
    cardurl = models.ImageField(upload_to='service_cardUrl/', null=True, blank=True, validators=[SVGValidator()])

    def __str__(self):
        return self.title

class ServiceFeature(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    feature = models.CharField(max_length=255)

    def __str__(self):
        return self.feature

class Hobby(models.Model):
    title = models.CharField(max_length=100)
    

    def __str__(self):
        return self.title

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=255)
    major = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.degree

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Project(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    github_link = models.URLField(null=True, blank=True)
    demo_link = models.URLField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='project_thumbnails/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    percentage = models.IntegerField(default=0, help_text='Percentage completion of the project')
    pricing = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Quote(models.Model):
    message = models.TextField()
    full_name = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=15)
    workEmail = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.timestamp