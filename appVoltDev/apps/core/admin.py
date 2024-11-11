from django.contrib import admin
from .models import PersonalImagen, PersonalCV, Projects, Tags
from import_export.resources import ModelResource
from import_export.admin import ExportActionModelAdmin, ImportExportModelAdmin

class TagsResource(ModelResource):
    class Meta:
        model = Tags
        use_bulk = True
        batch_size = 500


class ProjectsResource(ModelResource):
    class Meta:
        model = Projects
        use_bulk = True
        batch_size = 500


@admin.register(PersonalImagen)
class PersonalImagenAdmin(admin.ModelAdmin):
    pass


@admin.register(PersonalCV)
class PersonalCVAdmin(admin.ModelAdmin):
    pass


@admin.register(Projects)
class ProjectsAdmin(ImportExportModelAdmin, ExportActionModelAdmin):
    resource_classes = (ProjectsResource, )


@admin.register(Tags)
class TagsAdmin(ImportExportModelAdmin, ExportActionModelAdmin):
    resource_classes = (TagsResource, )
