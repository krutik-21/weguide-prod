"""myscholar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls 

API_TITLE = "Scholarship API"
API_DESCRIPTION = "APIs for fetching scholarship data."
schema_view = get_schema_view(title=API_TITLE)




urlpatterns = [
    path('admin/', admin.site.urls),

    #Django-Summernote
    path('summernote/',include('django_summernote.urls')),
    

    #REST FRAMEWORK URLS
    path('api/scholarship/',include('scholarships.api.urls')),
    path('api/ngo/',include('ngo.api.urls')),
    path('api/loans/',include('loans.api.urls')),
    path('api/bookbanks/',include('bookbanks.api.urls')),

    #API Docs
    path('docs/', include_docs_urls(title=API_TITLE,description=API_DESCRIPTION)), 
    path('schema/', schema_view),

    #PAGES URL
    path('',include('pages.urls')),
    
]


urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)





