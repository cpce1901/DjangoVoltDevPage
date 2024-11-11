from django.contrib import admin
from .models import PersonalImagen, PersonalCV, Projects, Tags

@admin.register(PersonalImagen)
class PersonalImagenAdmin(admin.ModelAdmin):
    pass

@admin.register(PersonalCV)
class PersonalCVAdmin(admin.ModelAdmin):
    pass

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    pass

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass
