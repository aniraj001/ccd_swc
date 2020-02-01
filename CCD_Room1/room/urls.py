from django.urls import path
from . import views

app_name = 'room'

urlpatterns = [
	# /music/
    path('', views.IndexView.as_view(), name='index'),

    path('register/', views.UserFormView.as_view(), name='register'),

	# /room/<company_id>/
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),

	# /room/company/add/
	path('company/add/', views.AlbumCreate.as_view(), name='company-add'),

	# /room/company/2/
	path('company/<int:pk>/', views.AlbumUpdate.as_view(), name='company-update'),

	# /room/company/2/delete/
	path('company/<int:pk>/delete/', views.AlbumDelete.as_view(), name='company-delete'),

]
