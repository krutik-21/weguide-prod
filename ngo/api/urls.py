from django.urls import path
from .views import (
    api_detail_ngo,
    api_list_active_ngo,
    api_filter_ngo,
    api_search_ngo,
    form_fields,
    crowdSourceView,
    getState)

app_name = 'Bookbank'

urlpatterns = [
    path('search/',api_search_ngo),
    path('filter/',api_filter_ngo.as_view()),   
    path('active/',api_list_active_ngo),
    path('active/<slug>/',api_detail_ngo),
    path('filterFields/',form_fields),
    path('crowdSource/',crowdSourceView),
    path('getState/',getState),
]