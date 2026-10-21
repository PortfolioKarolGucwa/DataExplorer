from django.urls import path

from . import views

urlpatterns = [
    path('', views.dataset_list, name='dataset_list'),
    path('upload/', views.upload_dataset, name='upload_dataset'),
    path('<int:pk>/delete/', views.delete_dataset, name='delete_dataset'),
]
