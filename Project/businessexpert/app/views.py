from django.shortcuts import render
from django.contrib import messages
from .models import Contact
# Create your views here.


def home_view(request):
    return render(request, "index.html")


def services_view(request):
    return render(request, "services.html")


def process_view(request):
    return render(request, "process.html")


def blog_view(request):
    return render(request, "blog.html")


def about_view(request):
    return render(request, "about.html")


def contact_view(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
    return render(request, "contact.html")
