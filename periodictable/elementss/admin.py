from django.contrib import admin
from .models import Element
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ElementResource(resources.ModelResource):
    class Meta:
        model = Element

class ElementAdmin(ImportExportModelAdmin):
    resource_class = ElementResource

admin.site.register(Element, ElementAdmin)