from django.shortcuts import render
from django.http import HttpResponse

from .models import Project, Category, Type
# Create your views here.
def index(request):
    categories = Category.objects.all()
    project_types = Type.objects.all()
    return render(request, 'sofiapp/index.html', {'categories': categories, 'project_types': project_types})
