from django.urls import path
from . import views

app_name = 'geeks'

urlpatterns = [
    path('create/', views.create_view, name='create'),
    path('list/', views.list_view, name='list'),
    path('detail/<int:id>/', views.detail_view, name='detail'),
    path('update/<int:id>/', views.update_view, name='update'),
    path('delete/<int:id>/', views.delete_view, name='delete'),
]
