from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Company, Hostel, Room
from .forms import UserForm

class IndexView(generic.ListView):
	template_name = 'room/index.html'
	context_object_name = 'all_companies'

	def get_queryset(self):
		return Company.objects.all()


class DetailView(generic.DetailView):
	model = Company
	template_name = 'room/detail.html'
	# context_object_name = 'all_rooms'

	# def get_queryset(self):
	# 	return Room.objects.all()



class CompanyCreate(CreateView):
	model = Company
	fields = ['company_name', 'industry', 'sector', 'company_logo']
	
class CompanyUpdate(UpdateView):
	model = Company
	fields = ['company_name', 'industry', 'sector', 'company_logo']

class CompanyDelete(DeleteView):
	model = Company
	success_url = reverse_lazy('room:index')


class UserFormView(View):
	form_class = UserForm
	template_name = 'room/registration_form.html'

	# Display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	# Process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			
			user = form.save(commit=False)
			
			# Cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			# returns User objects if credentials are correct
			user = authenticate(username=username, password=password)

			if user is not None:
				
				if user.is_active:
					login(request, user)
					#request.user.username
					#request.user.profile_photo
					return redirect('room:index')

		return render(request, self.template_name, {'form': form})









