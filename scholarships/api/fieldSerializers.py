from rest_framework import serializers
from scholarships.models import *

class StateSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = State
        fields = ['name']

class CourseSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Course
        fields = ['name']

class ReligionSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Religion
        fields = ['name']

class ClassSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Class
        fields = ['name']

class CountrySerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Country
        fields = ['name']

class GenderSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Gender
        fields = ['name']

class TypeSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Type
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Category
        fields = ['name']
