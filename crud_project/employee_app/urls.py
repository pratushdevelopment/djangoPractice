from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_employee, name='create_employee'),
    path('list/', views.employee_list, name='employee_list'),
    path('edit/<int:employee_id>/', views.edit_employee, name='edit_employee'), 
    path('delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
]