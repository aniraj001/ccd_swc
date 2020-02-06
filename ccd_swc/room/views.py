from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Company, Hostel, Room
# from .forms import UserForm

class IndexView(generic.ListView):
	template_name = 'company_list.html'
	model = Company

class DetailView(generic.DetailView):
	template_name = 'company_detail.html'
	model = Company

class ImageOneView(TemplateView):
	template_name = 'hostel_image1.html'

class ImageTwoView(TemplateView):
	template_name = 'hostel_image2.html'

class CompanyCreate(CreateView):
	template_name = 'companycreate.html'
	model = Company
	fields = ('name', 'industry', 'poc')
	success_url = reverse_lazy('room:index')
	# redirect_field_name = 'company_list.html'

class CompanyUpdate(UpdateView):
	model = Company
	fields = ('name', 'industry', 'poc')

class CompanyDelete(DeleteView):
	model = Company
	success_url = reverse_lazy('room:index')

def about(request):
    return render(request,'about.html',context=None)
