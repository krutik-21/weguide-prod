from django.urls import path
from .views import (
    api_detail_bookbank,
    api_list_active_bookbank,
    api_filter_bookbank,
    api_search_bookbank,
    form_fields,
    crowdSourceView,
    getDistrict)

app_name = 'bookbanks'

urlpatterns = [
    path('search/',api_search_bookbank),
    path('filter/',api_filter_bookbank.as_view()), 
    path('active/',api_list_active_bookbank),
    path('active/<slug>/',api_detail_bookbank),
    path('filterFields/',form_fields),
    path('crowdSource/',crowdSourceView),
    path('getDistrict/',getDistrict)
]