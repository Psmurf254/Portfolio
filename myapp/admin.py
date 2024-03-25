from django.contrib import admin
from .models import PersonalInfo, About, Language, Service, ServiceFeature, Hobby, Education, Experience, Project, Skill, Quote, ProjectNotification

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'gender', 'date_of_birth', 'contact_phone', 'contact_email', 'nationality']
    search_fields = ['full_name', 'contact_email']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'percentage']
    search_fields = ['title']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'pricing']
    search_fields = ['title']

@admin.register(ServiceFeature)
class ServiceFeatureAdmin(admin.ModelAdmin):
    list_display = ['service', 'feature']
    search_fields = ['feature']

@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'major', 'start_date', 'end_date']
    search_fields = ['degree', 'institution']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'location', 'start_date', 'end_date']
    search_fields = ['title', 'company']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date', 'status', 'percentage', 'pricing']
    search_fields = ['title']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'proficiency']
    search_fields = ['name']

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'message']
    search_fields = ['full_name']

@admin.register(ProjectNotification)
class ProjectNotificationAdmin(admin.ModelAdmin):
    list_display = ['project', 'email']
    search_fields = ['project']
