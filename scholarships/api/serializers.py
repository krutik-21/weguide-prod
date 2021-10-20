from rest_framework import serializers
from scholarships.models import Scholarship,CrowdSource

#Serializer for scholarship detail
class ScholarshipSerializer(serializers.ModelSerializer):
    sclass = serializers.StringRelatedField(many=True)  # Required to serialize foreign key relationships.
    state = serializers.StringRelatedField()            # many=True indicates many to many relation.
    course = serializers.StringRelatedField()
    religion = serializers.StringRelatedField()
    country = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    stype = serializers.StringRelatedField()
    gender = serializers.StringRelatedField(many=True)
    class Meta:
        model = Scholarship
        fields = '__all__'


#Serializer for scholarship list
class ScholarshipListSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Scholarship
        fields = ['title','image','slug','deadline','eligibility','award','updated_on']

class CrowdSourceSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = CrowdSource
        fields = '__all__'