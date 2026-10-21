from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.dataset_analysis, name='dataset_analysis'),
]
