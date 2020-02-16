from import_export import resources
from .models import Company,data

class CompanyResource(resources.ModelResource):
    class Meta:
        model = Company

class dataResource(resources.ModelResource):
	class Meta:
		model = data