from django.urls import path

from . import views

app_name = 'request'

urlpatterns = [
    path('', views.index, name='index'),
    path('warehouse/', views.warehouse, name='warehouse'),
    path('details/<int:id>/', views.details_request, name='details_request'),
    path('new request', views.new_request, name='new_request'),
    path('update request/<int:id>/', views.update_request, name='update_request'),
    path('search request/', views.search_request, name='search_request'),
]
