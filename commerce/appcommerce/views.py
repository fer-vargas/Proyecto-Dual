from django.shortcuts import render

# Create your views here.

def Inicio(request):
    return render(request, 'appcommerce/index.html')

def about(request):
    return render(request, 'appcommerce/about.html')

def services(request):
    return render(request, 'appcommerce/services.html')


def testimonials(request):
    return render(request, 'appcommerce/testimonials.html')

def contact(request):
    return render(request, 'appcommerce/contact.html')
