from django.urls import path
from . import views

app_name = 'room'

urlpatterns = [
    path('all_data/', views.export, name='export_data'),

    path('company/', views.export_company, name='export_company'),

    path('index/', views.search, name='index'),

	path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    path('<int:pk>/barak',views.room_list,name='roomlist'),

    path('<int:pk>/umium',views.room_list1,name='roomlist1'),

	path('add_company/', views.CompanyCreate.as_view(), name='company-add'),

	path('<int:pk>/company_update', views.CompanyUpdate.as_view(), name='company-update'),

	path('<int:pk>/company_delete/', views.CompanyDelete.as_view(), name='company-delete'),

    path('<int:pk>/barak/delete_room/', views.remove_room, name='room_remove'),

    path('<int:pk>/barak/add_rooms',views.add_room,name='roomadd'),

    path('<int:pk>/umium/delete_room/', views.remove_room1, name='room_remove1'),

    path('<int:pk>/umium/add_rooms',views.add_room1,name='roomadd1'),

    path('delete_all_rooms/',views.addrooms_delete,name='rooms_delete'),

]
