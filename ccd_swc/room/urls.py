from django.urls import path
from . import views

app_name = 'room'

urlpatterns = [
    path('all_data/', views.export, name='export_data'),

    path('company/', views.export_company, name='export_company'),

    path('', views.search, name='index'),

    path('', views.searching, name='index1'),

	path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    path('<int:pk>/roomlist',views.room_list,name='roomlist'),

    path('<int:pk>/roomlist1',views.room_list1,name='roomlist1'),

	path('add_company/', views.CompanyCreate.as_view(), name='company-add'),

	path('<int:pk>/company_update', views.CompanyUpdate.as_view(), name='company-update'),

	path('company/<int:pk>/delete/', views.CompanyDelete.as_view(), name='company-delete'),

    path('<int:pk>/delete_room/', views.remove_room, name='room_remove'),

    path('<int:pk>/add_room',views.add_room,name='roomadd'),

    path('<int:pk>/delete_room1/', views.remove_room1, name='room_remove1'),

    path('<int:pk>/add_room1',views.add_room1,name='roomadd1'),

    path('deleteall/',views.addrooms_delete,name='rooms_delete'),

]
