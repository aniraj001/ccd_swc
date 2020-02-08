from django.urls import path
from . import views

app_name = 'room'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('company/<int:pk>/rooms/image1', views.ImageOneView.as_view(), name='image1'),

    path('company/<int:pk>/rooms/image2', views.ImageTwoView.as_view(), name='image2'),

	path('<int:pk>/', views.DetailView.as_view(), name='detail'),

	path('company/add/', views.CompanyCreate.as_view(), name='company-add'),

	path('company/<int:pk>/', views.CompanyUpdate.as_view(), name='company-update'),

	path('company/<int:pk>/delete/', views.CompanyDelete.as_view(), name='company-delete'),

    path('company/<int:pk>/add_room', views.AddRoom.as_view(), name='add_room'),

    path('company/<int:pk>/roomadd',views.context_obj,name='roomadd'),

    path('company/<int:pk>/rooms/image1/roomno',views.new,name='room_'),

]
