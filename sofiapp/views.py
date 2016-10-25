from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

from .forms import ContactForm

from .models import Project, Category, Type
# Create your views here.
def index(request):
    categories = Category.objects.all()
    project_types = Type.objects.all()
    return render(request, 'sofiapp/index.html', {'categories': categories, 'project_types': project_types})

def contact(request):
    if(request.method == 'GET'):
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if(form.is_valid()):
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
                messages.success(request, 'Mensaje enviado')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('sofiapp:contact')
    return render(request, 'sofiapp/contact.html', {'form': form})
