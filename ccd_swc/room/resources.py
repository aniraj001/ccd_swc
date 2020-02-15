from import_export import resources
from .models import Room,Company,Hostel

class RoomResource(resources.ModelResource):
    class Meta:
        model = Room

class CompanyResource(resources.ModelResource):
    class Meta:
        model = Company

class HostelResource(resources.ModelResource):
    class Meta:
        model = Hostel
