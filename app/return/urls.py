from django.urls import path

from . import views

app_name = 'return'

urlpatterns = [
    path('return/', views.index_return, name='index_return'),
    path('warehouse return/', views.warehouse_return, name='warehouse_return'),
    path('details_return/<int:id>/', views.details_return, name='details_return'),
    path('new return', views.new_return, name='new_return'),
    path('update return/<int:id>/', views.update_return, name='update_return'),
    path('search return/', views.search_return, name='search_return'),
]
