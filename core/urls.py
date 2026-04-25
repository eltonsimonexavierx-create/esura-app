from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('estudante/', views.estudante_view, name='estudante_dash'),
    path('professor/', views.professor_view, name='professor_dash'),
    path('admin-esura/', views.admin_view, name='admin_dash'),
    path('logout/', views.logout_view, name='logout'),
]





