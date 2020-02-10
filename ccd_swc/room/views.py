from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Company, Hostel, Room
from .forms import RoomForm

class IndexView(generic.ListView):
	template_name = 'company_list.html'
	model = Company

class DetailView(generic.DetailView):
	template_name = 'company_detail.html'
	model = Company

# class AddRoom(CreateView):
# 	template_name = 'add_room.html'
# 	model = Room
# 	fields = ('company','room_no','hostel')
# 	success_url = reverse_lazy('room:index')
# 	def get_context_data(self,**kwargs):
# 			context = super().get_context_data(**kwargs)
# 			company = get_object_or_404(Company,pk=self.kwargs['pk'])
# 			context['company'] = company.name
# 			return context

def context_obj(request,pk):
	company = get_object_or_404(Company,pk=pk)
	if request.method == "POST":
		form = RoomForm(request.POST)
		if form.is_valid():
			r = form.save(commit=False)
			s = Hostel.objects.filter(name=r.hostel)
			t = Room(company=company,hostel=s[0],room_no=r.room_no)
			# print(r.company)
			t.save()
			return redirect('room:detail', pk=company.pk)
	else:
		form = RoomForm()
	return render(request,'add_room.html',{'form':form})

def new(request,pk):
	comp = get_object_or_404(Company,pk=pk)
	s = Hostel.objects.filter(name="Brahmaputra")
	t = Room(company = comp,hostel = s[0],room_no = "S103")
	t.save()
	return redirect('room:detail', pk=comp.pk)

class ImageOneView(TemplateView):
	template_name = 'hostel_image1.html'
	def get_context_data(self,**kwargs):
			context = super().get_context_data(**kwargs)
			company = get_object_or_404(Company,pk=self.kwargs['pk'])
			context['hostel'] = "Brahmaputra"
			context['company'] = company.name
			context['primary'] = company.pk
			return context


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
