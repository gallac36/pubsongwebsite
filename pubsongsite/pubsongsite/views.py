from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    #return HttpResponse ('homepage')
    return render(request, 'homepage.html')

def about (request):
#    return HttpResponse ('about')
    return render(request, 'about_page.html')

def contact (request):
#    return HttpResponse ('contact')
    return render(request, 'contact.html')
