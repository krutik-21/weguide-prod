from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class ScholarshipAdmin(SummernoteModelAdmin,):
    list_display = ('title','updated_on','deadline')
    search_fields=('title',)
    list_filter = ('sclass','course','updated_on','gender','stype','country','state','religion')
    summernote_fields = '__all__' 
 
class GenAdmin(SummernoteModelAdmin) :
    list_display = ('name',)

class CsAdmin(SummernoteModelAdmin):
    list_filter = ('reviewed',)
    search_fields=('title',)
    list_display = ('title','sub_date',)

admin.site.register(State,GenAdmin)
admin.site.register(Country,GenAdmin)
admin.site.register(Course,GenAdmin)
admin.site.register(Religion,GenAdmin)
admin.site.register(Gender,GenAdmin)
admin.site.register(Class,GenAdmin)
admin.site.register(Category,GenAdmin)
admin.site.register(Type,GenAdmin)
admin.site.register(Scholarship,ScholarshipAdmin)
admin.site.register(CrowdSource,CsAdmin)
