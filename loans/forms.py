from django.forms import ModelForm
from django_filters import rest_framework as filters
from .models import Loan
class LoanForm(ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'

class LoanFilter(filters.FilterSet):
    class Meta:
        model = Loan
        fields = ['state','category','district','loan_amount','religion','country','interest']