from django.forms import ModelForm
from django_filters import rest_framework as filters
from .models import Scholarship
class ScholarshipForm(ModelForm):
    class Meta:
        model = Scholarship
        fields = '__all__'

class ScholarshipFilter(filters.FilterSet):
    class Meta:
        model = Scholarship
        fields = ['state','category','sclass','stype','religion','course','gender']