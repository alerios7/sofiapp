from django.contrib import admin

from .models import Category, Image, Project, ProjectCategoryRelationship

# Register your models here.
class ImageInlineAdmin(admin.TabularInline):
    model = Image
    extra = 1

class ProjectCategoryRelationshipInline(admin.TabularInline):
    model = ProjectCategoryRelationship
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'text', 'project_type', 'created_date', 'public']})
    ]
    inlines = [ProjectCategoryRelationshipInline, ImageInlineAdmin,]

#class CategoryAdmin(admin.ModelAdmin):
#    inlines = [ProjectCategoryRelationshipInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
