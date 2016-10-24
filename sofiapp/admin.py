from django.contrib import admin

from .models import Type, Category, Image, Project, ProjectTypeM2M, ProjectCategoryRelationship

# Register your models here.
class ImageInlineAdmin(admin.TabularInline):
    model = Image
    extra = 1

class ProjectTypeM2MInline(admin.TabularInline):
    model = ProjectTypeM2M
    extra = 1

class ProjectCategoryRelationshipInline(admin.TabularInline):
    model = ProjectCategoryRelationship
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'text', 'location', 'architecture', 'landscaping', 'created_date', 'public']})
    ]
    inlines = [ProjectTypeM2MInline, ProjectCategoryRelationshipInline, ImageInlineAdmin,]

#class CategoryAdmin(admin.ModelAdmin):
#    inlines = [ProjectCategoryRelationshipInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Type)
admin.site.register(Category)
