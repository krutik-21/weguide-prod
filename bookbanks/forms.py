from django.forms import ModelForm
from django_filters import rest_framework as filters
from .models import Bookbank
class BookbankForm(ModelForm):
    class Meta:
        model = Bookbank
        fields = '__all__'

class BookbankFilter(filters.FilterSet):
    class Meta:
        model = Bookbank
        fields = ['state','district','books']