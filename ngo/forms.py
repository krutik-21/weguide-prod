from django.forms import ModelForm
from django_filters import rest_framework as filters
from .models import NGO
class NGOForm(ModelForm):
    class Meta:
        model = NGO
        fields = '__all__'

class NGOFilter(filters.FilterSet):
    class Meta:
        model = NGO
        fields = ['country','state','category','stype','religion','gender']