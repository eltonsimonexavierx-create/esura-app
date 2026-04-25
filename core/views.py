from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# 1. Função de Login (Processa o teu formulário de 120px)
def login_view(request):
    if request.method == 'POST':
        user_nome = request.POST.get('username')
        user_pass = request.POST.get('password')
        
        # Autentica o utilizador na base de dados
        user = authenticate(request, username=user_nome, password=user_pass)
        
        if user is not None:
            login(request, user)
            
            # Lógica de Redirecionamento por Perfil:
            if user.is_superuser:
                return redirect('admin_dash')
            elif user.groups.filter(name='Professor').exists():
                return redirect('professor_dash')
            else:
                return redirect('estudante_dash')
        else:
            # Se os dados estiverem errados, volta ao login com um aviso
            return render(request, 'login.html', {'erro': True})
            
    return render(request, 'login.html')

# 2. View do Painel do Estudante
def estudante_view(request):
    return render(request, 'estudante_dash.html')

# 3. View do Painel do Professor
def professor_view(request):
    return render(request, 'professor_dash.html')

# 4. View do Painel do Administrador
def admin_view(request):
    return render(request, 'admin_dash.html')

# 5. Função para Sair (Logout)
def logout_view(request):
    logout(request)
    return redirect('login')
