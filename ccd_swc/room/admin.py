from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Company,Hostel,Room
# Register your models here.
@admin.register(Company)
@admin.register(Hostel)
@admin.register(Room)

class ViewAdmin(ImportExportModelAdmin):
	pass
