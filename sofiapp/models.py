from django.db import models
from django.utils import timezone

# Create your models here.
#One project can have many categories, and one category can have many projects
class Type(models.Model):
    project_type = models.CharField('Tipo de proyecto', max_length=200, unique=True)

    def __str__(self):
        return self.project_type

class Category(models.Model):
    category_name = models.CharField('Nombre categoría', max_length=200, unique=True)

    def __str__(self):
        return self.category_name

# Project model
class Project(models.Model):
    title = models.CharField('Título', max_length=200)
    text = models.TextField('Descripción')
    project_types = models.ManyToManyField(Type, through='ProjectTypeM2M')
    created_date = models.DateField('Fecha de creación', default=timezone.now())
    architecture = models.CharField('Arquitectura', max_length=200, blank=True)
    landscaping = models.CharField('Paisajismo', max_length=200, blank=True)
    location = models.CharField('Ubicación', max_length=200)
    categories = models.ManyToManyField(Category, through='ProjectCategoryRelationship')
    public = models.BooleanField('Proyecto público', default=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField('Imagen', upload_to='project_images/')
    project = models.ForeignKey(Project , related_name='images', blank=True, null=True)

    def __str__(self):
        return self.filename

    @property
    def filename(self):
        return self.image.name.rsplit('/', 1)[-1]


class ProjectTypeM2M(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    project_type = models.ForeignKey(Type, on_delete=models.CASCADE)

class ProjectCategoryRelationship(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
