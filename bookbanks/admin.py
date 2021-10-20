from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class BookbankAdmin(SummernoteModelAdmin,):
    list_display = ('title','updated_on',)
    search_fields=('title',)
    list_filter = ('updated_on','state','district','books')
    summernote_fields = '__all__' 
 
class GenAdmin(SummernoteModelAdmin) :
    list_display = ('name',)

class CsAdmin(SummernoteModelAdmin):
    list_filter = ('reviewed',)
    search_fields=('title',)
    list_display = ('title','sub_date',)

admin.site.register(State,GenAdmin)
admin.site.register(District,GenAdmin)
admin.site.register(Books,GenAdmin)

admin.site.register(Bookbank,BookbankAdmin)
admin.site.register(CrowdSource,CsAdmin)
