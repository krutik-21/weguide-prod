from rest_framework import serializers
from loans.models import Loan,CrowdSource

#Serializer for loan detail
class LoanSerializer(serializers.ModelSerializer): 
    state = serializers.StringRelatedField()            # Required to serialize foreign key relationships. 
    district = serializers.StringRelatedField()         # many=True indicates many to many relation.
    religion = serializers.StringRelatedField()
    country = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    LoanAmt = serializers.StringRelatedField()
    class Meta:
        model = Loan
        fields = '__all__'


#Serializer for loan list
class LoanListSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Loan
        fields = ['title','slug','eligibility','award','updated_on']

class CrowdSourceSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = CrowdSource
        fields = '__all__'