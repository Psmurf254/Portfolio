from django.urls import path
from . import views

urlpatterns = [
    path('personalinfo/', views.getPersonalInfo),
    path('personal-info/<int:pk>/', views.PersonalInfoRetrieveUpdateDestroy.as_view()),
    path('about/', views.getAbout),
    path('about/add/', views.add_About),
    path('about/update/<int:pk>/', views.AboutRetrieveUpdateDestroy.as_view()),
    path('languages/', views.getLanguages),
    path('language/add/', views.add_Language),
    path('language/update/<int:pk>/', views.LanguageRetrieveUpdateDestroy.as_view()),
    path('services/', views.getServices),
    path('service/add/', views.add_Service),
    path('services/update/<int:pk>/', views.ServiceRetrieveUpdateDestroy.as_view()),
    path('hobbies/', views.getHobbies),
    path('hobbie/add/', views.add_Hobbie),
    path('hobbie/update/<int:pk>/', views.HobbyRetrieveUpdateDestroy.as_view()),
    path('education/', views.getEducation),
    path('education/<int:pk>/', views.EducationRetrieveUpdateDestroy.as_view()),
    path('experiences/', views.getExperiences),
    path('experiences/<int:pk>/', views.ExperienceRetrieveUpdateDestroy.as_view()),
    path('projects/', views.getProjects),
    path('projects/add/', views.add_project),
    path('project/update/<int:pk>/', views.ProjectUpdateRetrieveUpdateDestroyView.as_view()),

    path('skills/', views.getSkills),
    path('skills/<int:pk>/', views.SkillRetrieveUpdateDestroy.as_view()),

    path('contacts/', views.getContacts),
    path('contacts/<int:pk>/', views.QuoteRetrieveUpdateDestroy.as_view()),
    path('create_quote/', views.Create_Quote, name='create_quote'),


]
