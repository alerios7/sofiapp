from django.db import models
from django.utils import timezone

# Create your models here.
#One project can have many categories, and one category can have many projects
class Category(models.Model):
    category_name = models.CharField('Nombre categoría', max_length=200, unique=True)

    def __str__(self):
        return self.category_name

# Project model
class Project(models.Model):
    PROJECT_TYPE = (
        ('I', 'Iluminación'),
        ('P', 'Paisajismo'),
        ('M', 'Mixto'),
    )

    title = models.CharField('Título', max_length=200)
    text = models.TextField('Descripción')
    project_type = models.CharField('Tipo', max_length=1, choices=PROJECT_TYPE, default='I')
    created_date = models.DateTimeField(default=timezone.now())
    categories = models.ManyToManyField(Category, through='ProjectCategoryRelationship')

    def __str__(self):
        return self.title

class ProjectCategoryRelationship(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
