from rest_framework import serializers
from .models import PersonalInfo, About, Language, Service, ServiceFeature, Hobby, Education, Experience, Project, Skill, Quote, ProjectNotification

class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = '__all__'

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class ServiceFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceFeature
        fields = '__all__'

# serializers.py

class ServiceSerializer(serializers.ModelSerializer):
    features = serializers.StringRelatedField(source='servicefeature_set', many=True)

    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'pricing', 'image', 'features']


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    def update(self, instance, validated_data):
        thumbnail = validated_data.pop('thumbnail', None)
        instance = super().update(instance, validated_data)
        if thumbnail:
            instance.thumbnail = thumbnail
            instance.save()
        return instance


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'

class ProjectNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectNotification
        fields = '__all__'

