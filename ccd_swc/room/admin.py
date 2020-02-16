from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Company,Hostel,Room,data
# Register your models here.
@admin.register(Company)
@admin.register(Hostel)
@admin.register(Room)
@admin.register(data)

class ViewAdmin(ImportExportModelAdmin):
	pass
