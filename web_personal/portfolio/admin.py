from django.contrib import admin
from . import models

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']


admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Author)
