from django.urls import path
from .views import (
    api_detail_scholarship,
    api_list_active_scholarship,
    api_list_inactive_scholarship,
    #api_state_list_scholarship,
    #api_class_list_scholarship,
    #api_type_list_scholarship,
    #api_category_list_scholarship,
    api_filter_scholarship,
    api_search_scholarship,
    form_fields,
    crowdSourceView,
    getState)

app_name = 'scholarships'

urlpatterns = [
    path('search/',api_search_scholarship),
    path('filter/',api_filter_scholarship.as_view()),   
    #path('category/<str:category>/',api_category_list_scholarship),  
    #path('type/<str:stype>/',api_type_list_scholarship),    
    #path('class/<str:sclass>/',api_class_list_scholarship), 
    #path('state/<str:state>/',api_state_list_scholarship),
    path('inactive/',api_list_inactive_scholarship),
    path('active/',api_list_active_scholarship),
    path('active/<slug>/',api_detail_scholarship),
    path('filterFields/',form_fields),
    path('crowdSource/',crowdSourceView),
    path('getState/',getState),
]