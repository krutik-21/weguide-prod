from django.urls import path
from .views import (
    api_list_active_loan,
    api_filter_loan,
    api_search_loan,
    form_fields,
    crowdSourceView,
    getState,
    getDistrict)

app_name = 'loans'

urlpatterns = [
    path('search/',api_search_loan),
    path('filter/',api_filter_loan.as_view()),      
    path('active/',api_list_active_loan),
    path('filterFields/',form_fields),
    path('crowdSource/',crowdSourceView),
    path('getState/',getState),
    path('getDistrict/',getDistrict)
]