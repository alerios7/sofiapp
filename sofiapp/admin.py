from django.contrib import admin

from .models import Category, Project, ProjectCategoryRelationship

# Register your models here.

class ProjectCategoryRelationshipInline(admin.TabularInline):
    model = ProjectCategoryRelationship
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'text', 'project_type', 'created_date']})
    ]
    inlines = [ProjectCategoryRelationshipInline]

#class CategoryAdmin(admin.ModelAdmin):
#    inlines = [ProjectCategoryRelationshipInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
