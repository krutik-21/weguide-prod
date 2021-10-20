from rest_framework import serializers
from ngo.models import NGO,CrowdSource

#Serializer for scholarship detail
class NGOSerializer(serializers.ModelSerializer):  
    state = serializers.StringRelatedField()           # Required to serialize foreign key relationships.  
    religion = serializers.StringRelatedField()
    country = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    stype = serializers.StringRelatedField()
    gender = serializers.StringRelatedField(many=True) # many=True indicates many to many relation.
    class Meta:
        model = NGO
        fields = '__all__'


#Serializer for scholarship list
class NGOListSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = NGO
        fields = ['title','slug','eligibility','updated_on']

class CrowdSourceSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = CrowdSource
        fields = '__all__'