# En views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Usuario

from django.contrib.auth.decorators import login_required
from .models import Docente, Funcionario


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
def login_view(request):
    if request.method == 'POST':
        # Obtener el nombre de usuario y la contraseña del formulario
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verificar si el nombre de usuario y la contraseña están presentes
        if username and password:
            # Intentar autenticar al usuario
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Usuario autenticado correctamente, realizar redireccionamiento
                login(request, user)
                if user.tipo_usuario == Usuario.DOCENTE:
                    return redirect('docente_home')
                elif user.tipo_usuario == Usuario.FUNCIONARIO:
                    return redirect('funcionario_home')
            else:
                # Las credenciales son inválidas, renderizar el formulario de inicio de sesión con un mensaje de error
                return render(request, 'login.html', {'error_message': 'Invalid username or password'})
        else:
            # Los campos del formulario no están presentes, renderizar el formulario de inicio de sesión con un mensaje de error
            return render(request, 'login.html', {'error_message': 'Username and password are required'})

    # Si el método de la solicitud no es POST o no se proporcionaron credenciales, renderizar el formulario de inicio de sesión
    return render(request, 'login.html')

@login_required
def docente_home(request):
    # Obtener el objeto Docente asociado al usuario actual
    docente = Docente.objects.get(usuario=request.user)
    # Aquí puedes realizar cualquier lógica específica para el docente
    # Por ejemplo, obtener información adicional del docente o realizar operaciones relacionadas con su perfil
    return render(request, 'docente_home.html', {'docente': docente})

@login_required
def funcionario_home(request):
    # Obtener el objeto Funcionario asociado al usuario actual
    funcionario = Funcionario.objects.get(usuario=request.user)
    # Aquí puedes realizar cualquier lógica específica para el funcionario
    # Por ejemplo, obtener información adicional del funcionario o realizar operaciones relacionadas con su perfil
    return render(request, 'funcionario_home.html', {'funcionario': funcionario})