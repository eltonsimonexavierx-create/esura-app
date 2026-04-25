from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Função principal do teu Login Ultra Magro
def login_view(request):
    if request.method == 'POST':
        user_nome = request.POST.get('username')
        user_pass = request.POST.get('password')
        
        user = authenticate(request, username=user_nome, password=user_pass)
        
        if user is not None:
            login(request, user)
            # Lógica de perfis:
            if user.is_superuser:
                return redirect('admin_dash')
            elif user.groups.filter(name='Professor').exists():
                return redirect('professor_dash')
            else:
                return redirect('estudante_dash')
        else:
            # Se falhar, recarrega o login
            return render(request, 'login.html', {'error': True})
            
    return render(request, 'login.html')

# Views temporárias para os Dashboards
def estudante_view(request):
    return render(request, 'estudante_dash.html')

def professor_view(request):
    return render(request, 'professor_dash.html')

def admin_view(request):
    return render(request, 'admin_dash.html')
