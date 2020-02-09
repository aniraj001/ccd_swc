from django.urls import path
from . import views

app_name = 'room'

urlpatterns = [

    path('', views.search, name='index'),

    path('<int:pk>/brahmaputra', views.ImageOneView.as_view(), name='image1'),

    path('<int:pk>/lohit', views.ImageTwoView.as_view(), name='image2'),

	path('<int:pk>/', views.DetailView.as_view(), name='detail'),

	path('add_company/', views.CompanyCreate.as_view(), name='company-add'),

	path('<int:pk>/company_update', views.CompanyUpdate.as_view(), name='company-update'),

	path('company/<int:pk>/delete/', views.CompanyDelete.as_view(), name='company-delete'),

    path('<int:pk>/delete_room/', views.remove_room, name='room_remove'),

    path('<int:pk>/add_room',views.context_obj,name='roomadd'),

    path('<int:pk>/brahmaputra/room_no',views.new,name='room_'),

]
