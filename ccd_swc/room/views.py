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

class AddRoom(CreateView):
	template_name = 'add_room.html'
	model = Room
	fields = ('room_no', 'hostel')

	def __init__(self):
		company = self.request.GET.get('company')
		return {'company':company}
		# initial = super(AddRoom,self).get_initial()
		# initial['company'] = Company.objects.get(pk=self.kwargs['pk'])
		# return initial

	success_url = reverse_lazy('room:index')

class ImageOneView(TemplateView):
	template_name = 'hostel_image1.html'

class ImageTwoView(TemplateView):
	template_name = 'hostel_image2.html'

class CompanyCreate(CreateView):
	template_name = 'companycreate.html'
	model = Company
	fields = ('name', 'industry', 'poc')
	success_url = reverse_lazy('room:index')

class CompanyUpdate(UpdateView):
	model = Company
	fields = ('name', 'industry', 'poc')

class CompanyDelete(DeleteView):
	model = Company
	success_url = reverse_lazy('room:index')

def about(request):
    return render(request,'about.html',context=None)
