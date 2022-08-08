from datetime import datetime
import imp
from django.contrib import admin
from pytz import timezone
from activity_dashboard.models import KDS, FIORI, PERIPHERALS, UNITTEST, UTMASTER
from import_export.admin import ExportActionMixin, ImportExportModelAdmin
from import_export import resources
from django.utils.timezone import localtime, now
# Register your models here.

class KDSResource(resources.ModelResource):
    class Meta:
        model = KDS
        
class UTResource(resources.ModelResource):
    class Meta:
        model = UNITTEST
        

excl_editable_kds =['link','created_by','created_on','updated_by','updated_on']


class KDSAdmin(ImportExportModelAdmin, ExportActionMixin):#, admin.ModelAdmin):
    resource_class = KDSResource
    list_of_fields = [field.name for field in KDS._meta.fields if field.name not in "id"] 
    list_display = list_of_fields
    list_display_links = ['link']
    #list_editable=  [field for field in list_of_fields if field not in excl_editable_kds]
    list_filter = ['master_name', 'section']
    search_fields = ['name_of_field']
    readonly_fields=['link', 'created_by','created_on','updated_by','updated_on']
    fieldsets = (
        ('Field Details',{
            'fields':('name_of_field','purpose', 
                        'master_name','section', 'data_type', 
                        'type_of_field', 'possible_sources', 'legacy_field')
        }),
        ('Grouping',{
            'fields':(('group_1','group_2','group_3'))
        }),
        ('Field Utility',{
            'fields':('sbu','customer_type')
        }),
        ('MDG Rules',{
            'fields':('mdg_rules_1', 'mdg_rules_2','mdg_rules_3','mdg_rules_4',
                            'mdg_rules_5')
        }),
        ('Team Inputs',{
            'fields':('action', 'comments')
        }),  
        ('User Data',{
            'fields':('created_by', 'created_on', 'updated_by', 'updated_on')
        }),  
    )

    def save_model(self, request, obj, form, change):
        print(request.user)
        if not obj.id:
            obj.created_by = str(request.user)
            obj.created_on = now()
        obj.updated_by = str(request.user)
        obj.updated_on = now()
        super().save_model(request, obj, form, change)
    
class UTMASTERAdmin(ImportExportModelAdmin, ExportActionMixin):
    list_display = ['test_case_id']
    
class UTAdmin(ImportExportModelAdmin, ExportActionMixin):#, admin.ModelAdmin):
    resource_class = UTResource
    list_display = [field.name for field in UNITTEST._meta.fields if field.name not in "id"] 
    #list_filter = ['unit_test']#, 'owner']
    #search_fields = ['data']
    readonly_fields=['created_by','created_on','updated_by','updated_on']
    def save_model(self, request, obj, form, change):
        print(request.user)
        if not obj.id:
            obj.created_by = str(request.user)
            obj.created_on = now()
        obj.updated_by = str(request.user)
        obj.updated_on = now()
        super().save_model(request, obj, form, change)


class FIORIAdmin(admin.ModelAdmin):
    pass

class PERIPHERALSAdmin(admin.ModelAdmin):
    pass

admin.site.register(KDS,KDSAdmin)
admin.site.register(FIORI,FIORIAdmin)
admin.site.register(PERIPHERALS,PERIPHERALSAdmin)
admin.site.register(UNITTEST,UTAdmin)
admin.site.register(UTMASTER,UTMASTERAdmin)


admin.site.site_header = 'Sales Dashboard'                    # default: "Django Administration"
admin.site.index_title = 'Backoffice'                 # default: "Site administration"
admin.site.site_title = 'Sales Team' # default: "Django site admin"