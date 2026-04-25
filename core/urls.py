from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('estudante/', views.estudante_view, name='estudante_dash'),
    path('professor/', views.professor_view, name='professor_dash'),
    path('admin-esura/', views.admin_view, name='admin_dash'),
]
