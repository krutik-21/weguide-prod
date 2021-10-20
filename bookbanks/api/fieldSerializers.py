from rest_framework import serializers
from bookbanks.models import *

class StateSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = State
        fields = ['name']

class DistrictSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = District
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Books
        fields = ['name']





