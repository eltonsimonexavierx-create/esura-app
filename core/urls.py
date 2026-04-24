from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

def login_view(request):
    return render(request, 'login.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
]

# Esta linha força o Django a encontrar as imagens na pasta static
if settings.DEBUG or True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
