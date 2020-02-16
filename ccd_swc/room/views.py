from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import  CreateView, UpdateView, DeleteView, FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Company, Hostel, Room, data
from .forms import FilebabyForm,RoomForm
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .resources import CompanyResource, dataResource
import sqlite3

def export_company(request):
	company_resource = CompanyResource()
	dataset = company_resource.export()
	response = HttpResponse(dataset.csv, content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="companies.csv"'
	return response

def export(request):
	for room in Room.objects.all():
		data.objects.create(company=room.company.name,hostel=room.hostel.name,room_no=room.room_no)
	data_resource = dataResource()
	dataset = data_resource.export()
	response = HttpResponse(dataset.csv, content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="all_data.csv"'
	data.objects.all().delete()
	return response

class DetailView(generic.DetailView):
	template_name = 'company_detail.html'
	model = Company

def addrooms_delete(request):
	results = Company.objects.all()
	if request.method == 'POST':
		Room.objects.all().delete()
		return render(request,'company_list.html',{'data':results})
	else:
		return render(request,'allrooms_confirm_delete.html')

def room_list(request,pk):
	company = get_object_or_404(Company,pk=pk)
	s = Hostel.objects.filter(name="Barak")
	ro = Room.objects.filter(hostel=s[0])
	return render(request,'company_roomlist.html',{'roomlist':ro,'hostel':"Barak"})

def room_list1(request,pk):
	company = get_object_or_404(Company,pk=pk)
	s = Hostel.objects.filter(name="Umiam")
	ro = Room.objects.filter(hostel=s[0])
	return render(request,'company_roomlist.html',{'roomlist':ro,'hostel':"Umiam"})

def search(request):
	query = request.GET.get('q','')
	if query:
		results = Company.objects.filter(name__istartswith=query)
	else:
		results = Company.objects.all()
	return render(request, 'company_list.html', {'data':results})

def add_room(request,pk):
	company = get_object_or_404(Company,pk=pk)
	s = Hostel.objects.filter(name="Barak")
	ro = Room.objects.filter(hostel=s[0])

	if request.method == "POST":
		rooms = request.POST['roo']
		l = rooms.split()
		for room in l:
			Room.objects.create(company=company,hostel=s[0],room_no=room)
		return redirect('room:detail', pk=company.pk)
	else:
		form = RoomForm()
	return render(request,'add_room.html',{'form':form,'primary':pk,'rooms':ro})

@login_required
def remove_room(request,pk):
	comp = get_object_or_404(Company,pk=pk)
	if request.method == 'POST':
		form = RoomForm(request.POST)
		room = request.POST.get('room_no')
		k = Hostel.objects.filter(name="Barak")
		dk = Room.objects.filter(company=comp,hostel=k[0],room_no=room)
		if not dk:
			return HttpResponse("<h1 style='text-align:center;margin-top:20px;'>Room Number " + room + " is not alloted to " + comp.name + " in " + "Barak Hostel</h1>")
		dk.delete()
		return redirect('room:detail', pk=comp.pk)
	else:
		form = RoomForm()
	return render(request,'room_delete.html',context={'form':form})


def add_room1(request,pk):
	company = get_object_or_404(Company,pk=pk)
	s = Hostel.objects.filter(name="Umiam")
	ro = Room.objects.filter(hostel=s[0])

	if request.method == "POST":
		rooms = request.POST['roo']
		l = rooms.split()
		for room in l:
			Room.objects.create(company=company,hostel=s[0],room_no=room)
		return redirect('room:detail', pk=company.pk)
	else:
		form = RoomForm()
	return render(request,'add_room1.html',{'form':form,'primary':pk,'rooms':ro})

def remove_room1(request,pk):
	comp = get_object_or_404(Company,pk=pk)
	if request.method == 'POST':
		form = RoomForm(request.POST)
		room = request.POST.get('room_no')
		k = Hostel.objects.filter(name="Umiam")
		dk = Room.objects.filter(company=comp,hostel=k[0],room_no=room)
		if not dk:
			return HttpResponse("<h1 style='text-align:center;margin-top:20px;'>Room Number " + room + " is not alloted to "
			+ comp.name + " in " + "Umiam Hostel</h1>")
		dk.delete()
		return redirect('room:detail', pk=comp.pk)
	else:
		form = RoomForm()
	return render(request,'room_delete1.html',context={'form':form})

class CompanyCreate(LoginRequiredMixin,CreateView):
	login_url = '/login/'
	template_name = 'companycreate.html'
	model = Company
	fields = ('name', 'industry', 'poc')
	success_url = reverse_lazy('room:index')

class CompanyUpdate(LoginRequiredMixin,UpdateView):
	login_url = '/login/'
	template_name = 'companycreate.html'
	model = Company
	fields = ('name', 'industry', 'poc')

class CompanyDelete(LoginRequiredMixin,DeleteView):
	login_url = '/login/'
	model = Company
	success_url = reverse_lazy('room:index')

def about(request):
    return render(request,'about.html',context=None)
