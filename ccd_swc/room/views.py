from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import  CreateView, UpdateView, DeleteView, FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Company, Hostel, Room
from .forms import RoomForm, FilebabyForm
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class DetailView(generic.DetailView):
	template_name = 'company_detail.html'
	model = Company

def search(request):
    query = request.GET.get('q','')
    if query:
            results = Company.objects.filter(name=query)
    else:
       results = Company.objects.all()
    return render(request, 'company_list.html', {'results':results})

@login_required
def add_room(request,pk):
	company = get_object_or_404(Company,pk=pk)
	s = Hostel.objects.filter(name="Brahmaputra")
	ro = Room.objects.filter(company=company,hostel=s[0])
	if request.method == "POST":
		hostel = request.POST['hostel']
		rooms = request.POST['roo']
		s = Hostel.objects.filter(name=hostel)
		l = rooms.split()
		for room in l:
			Room.objects.create(company=company,hostel=s[0],room_no=room)
			print(room)
		return redirect('room:detail', pk=company.pk)
	else:
		form = RoomForm()
	return render(request,'add_room.html',{'form':form,'primary':pk,'rooms':ro})

@login_required
def remove_room(request,pk):
	comp = get_object_or_404(Company,pk=pk)
	if request.method == 'POST':
		form = RoomForm(request.POST)
		h = request.POST.get('hostel')
		room = request.POST.get('room_no')
		if h =="1":
			k = Hostel.objects.filter(name="Brahmaputra")
		else:
			k = Hostel.objects.filter(name="Lohit")
		Room.objects.filter(company=comp,hostel=k[0],room_no=room).delete()
		return redirect('room:detail', pk=comp.pk)
	else:
		form = RoomForm()
	return render(request,'room_delete.html',context={'form':form})

class ImageOneView(TemplateView):
	template_name = 'clickbox.html'
	def get_context_data(self,**kwargs):
			context = super().get_context_data(**kwargs)
			company = get_object_or_404(Company,pk=self.kwargs['pk'])
			s = Hostel.objects.filter(name="Brahmaputra")
			rooms = Room.objects.filter(company=company,hostel=s[0])
			context['hostel'] = "Brahmaputra"
			context['company'] = company.name
			context['primary'] = company.pk
			context['rooms'] = rooms
			return context

class CompanyCreate(LoginRequiredMixin,CreateView):
	login_url = '/login/'
	template_name = 'companycreate.html'
	model = Company
	fields = ('name', 'industry', 'poc','logo')
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
