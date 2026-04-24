from django.contrib import admin
from django.urls import path
from django.shortcuts import render

# Esta função carrega a página de login que vamos criar
def login_view(request):
    return render(request, 'login.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
]
