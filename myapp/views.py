from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.utils import timezone
from datetime import datetime
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Personal Info
@api_view(['GET'])
def getPersonalInfo(request):
    try:
        person = PersonalInfo.objects.all()
        serializer = PersonalInfoSerializer(person, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Exception as e:
        print('error', error_message)
        error_message = f"Error retrieving data: {str(e)}"
        return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class PersonalInfoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer


# About
@api_view(['GET'])
def getAbout(request):
    try:
        about = About.objects.all()
        serializer = AboutSerializer(about, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        error_message = f"Error retrieving data: {str(e)}"
        return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class AboutRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_About(request):
    try:
        recieved_data = request.data

        serializer = AboutSerializer(data=recieved_data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('Validation Error:', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        print('Error:', str(e))
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




# Language
@api_view(['GET'])
def getLanguages(request):
    try:
        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        error_message = f"Error retrieving data: {str(e)}"
        return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class LanguageRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_Language(request):
    try:

        received_data = request.data
     

        item_id = received_data.get('id')
       

        if item_id:
          
            language = Language.objects.get(pk=item_id)
            serializer = LanguageSerializer(language, data=received_data, partial=True)
        else:
           
            serializer = LanguageSerializer(data=received_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('Validation Error:', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Language.DoesNotExist:
        serializer = LanguageSerializer(data=received_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('Validation Error:', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        print('Error:', str(e))
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Service
@api_view(['GET'])
def getServices(request):
    try:
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        error_message = f"Error retrieving data: {str(e)}"
        return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class ServiceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_Service(request):
    try:

        received_data = request.data
     

        item_id = received_data.get('id')
       

        if item_id:
          
            service = Service.objects.get(pk=item_id)
            serializer = ServiceSerializer(service, data=received_data, partial=True)
        else:
           
            serializer = ServiceSerializer(data=received_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('Validation Error:', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Service.DoesNotExist:
        print('Project not found. Creating a new project.')
        serializer = ServiceSerializer(data=received_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('Validation Error:', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        print('Error:', str(e))
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
# Hobby
@api_view(['GET'])
def getHobbies(request):
    try:
        hobbies = Hobby.objects.all()
        serializer = HobbySerializer(hobbies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        error_message = f"Error retrieving data: {str(e)}"
        return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class HobbyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hobby.objects.all()
    serializer_class = HobbySerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_Hobbie(request):
    try:
        recieved_data = request.data

        serializer = HobbySerializer(data=recieved_data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('Validation Error:', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        print('Error:', str(e))
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Education
@api_view(['GET'])
def getEducation(request):
    try:
        education = Education.objects.all()
        serializer = EducationSerializer(education, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        error_message = f"Error retrieving data: {str(e)}"
        return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class EducationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


# Experience
@api_view(['GET'])
def getExperiences(request):
    try:
        experiences = Experience.objects.all()
        serializer = ExperienceSerializer(experiences, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        error_message = f"Error retrieving data: {str(e)}"
        return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class ExperienceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


# Project
@api_view(['GET'])
def getProjects(request):
    try:
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        error_message = f"Error retrieving data: {str(e)}"
        return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    



    
class ProjectUpdateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    

    
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_project(request):
    try:
        print('Request data:', request.data)

        received_data = request.data
        print('Received data:', received_data)

        project_id = received_data.get('id')
        print('Project ID:', project_id)

        if project_id:
            # Update existing project
            project = Project.objects.get(pk=project_id)
            serializer = ProjectSerializer(project, data=received_data, partial=True)
        else:
            # Create new project
            serializer = ProjectSerializer(data=received_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('Validation Error:', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Project.DoesNotExist:
        print('Project not found. Creating a new project.')
        serializer = ProjectSerializer(data=received_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('Validation Error:', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        print('Error:', str(e))
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Skill
@api_view(['GET'])
def getSkills(request):
    try:
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        error_message = f"Error retrieving data: {str(e)}"
        return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class SkillRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

#Contacts
@api_view(['GET'])
def getContacts(request):
    try:
        quotes = Quote.objects.all()
        serializer = QuoteSerializer(quotes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        error_message = f"Error retrieving data: {str(e)}"
        return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class QuoteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


@api_view(['POST'])
def Create_Quote(request):
    try:
        recieved_data = request.data
        recieved_data['timestamp'] = timezone.now()
        serializer = QuoteSerializer(data=recieved_data)

        if serializer.is_valid():
            serializer.save()
            print('Quote saved')
           
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('Validation Error:', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)