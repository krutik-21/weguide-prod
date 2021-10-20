from rest_framework import serializers
from bookbanks.models import Bookbank,CrowdSource

#Serializer for bookbank detail
class BookbankSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)  # Required to serialize foreign key relationships.
    state = serializers.StringRelatedField()            # many=True indicates many to many relation.
    district = serializers.StringRelatedField()

    class Meta:
        model = Bookbank
        fields = '__all__'


#Serializer for bookbank list
class BookbankListSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Bookbank
        fields = ['title','slug','updated_on']

#Serializer for crowd source 
class CrowdSourceSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = CrowdSource
        fields = '__all__'