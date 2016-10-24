from django.shortcuts import render
from django.http import HttpResponse

from .models import Project, Category
# Create your views here.
def index(request):
    categories = Category.objects.all()
    return render(request, 'sofiapp/index.html', {'categories': categories})
