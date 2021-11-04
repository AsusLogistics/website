from django.shortcuts import render
from .models import *
from django.http import HttpResponse, JsonResponse, FileResponse, Http404

# Create your views here.
def Landing_Page(request):
    return render(request, 'Landing Page.html')
