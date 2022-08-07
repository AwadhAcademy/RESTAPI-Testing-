from django.contrib import admin
from import_export.admin import ImportExportMixin
from . models import collection
# Register your models here.
@admin.register(collection)
class projectAdmin(ImportExportMixin, admin.ModelAdmin):
    pass