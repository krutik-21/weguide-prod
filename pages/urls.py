from django.urls import path,include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"),name = 'home'),
    path('ngos/',TemplateView.as_view(template_name ="ngo.html"),name = 'ngos'),
    path('scholarships/',TemplateView.as_view(template_name ="scholarship.html"),name = 'scholarships'),
    path('books/',TemplateView.as_view(template_name ="book.html"),name = 'books'),
    path('faq/',TemplateView.as_view(template_name ="faq.html"),name = 'faq'),
    path('loans/',TemplateView.as_view(template_name ="loans.html"),name = 'loans'),
    path('crowdsourcing/',TemplateView.as_view(template_name ="crowdsourcing.html"),name = 'crowdsourcing'),
    path('aboutus/',TemplateView.as_view(template_name ="aboutus.html"),name = 'about'),

]