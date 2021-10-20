from rest_framework import serializers
from loans.models import *

class StateSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = State
        fields = ['name']


class ReligionSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Religion
        fields = ['name']


class CountrySerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Country
        fields = ['name']



class CategorySerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Category
        fields = ['name']

class DistrictSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = District
        fields = ['name']

class LoanAmtSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = LoanAmt
        fields = ['name']
