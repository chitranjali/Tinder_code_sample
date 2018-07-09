from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Adult
from import_export import resources
# Register your models here.
# admin.site.register(Adult)

@admin.register(Adult)
class AdultAdmin(ImportExportModelAdmin):

    def get_resource_class(self):
        return AdultResource

class AdultResource(resources.ModelResource):

    class Meta:
        model = Adult
        # exclude = ('id',)
        import_id_fields = ('fnlwgt',)

