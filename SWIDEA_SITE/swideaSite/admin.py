# Register your models here.
# admin.py
from django.contrib import admin
from .models import Idea
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class IdeaResource(resources.ModelResource):
	class Meta:
		model = Idea
		fields = ('id', 'title', 'image', 'content', 'interest', 'devtool')
		export_order = fields


class IdeaAdmin(ImportExportModelAdmin):
	fields = ('title', 'image', 'content', 'interest', 'devtool')
	list_display = ('id', 'title', 'image', 'content', 'interest', 'devtool')
	resource_class = IdeaResource


admin.site.register(Idea, IdeaAdmin)