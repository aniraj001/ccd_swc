from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader

def index(request):
	return HttpResponse("<h1>Know more about us <a href = 'https://www.iitg.ac.in/ccd/'>here</a></h1><br><a href = 'http://127.0.0.1:8000/'>Go Back</a>")