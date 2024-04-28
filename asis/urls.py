from django.urls import path


from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('docente/', views.docente_home, name='docente_home'),
    path('funcionario/', views.funcionario_home, name='funcionario_home'),
    # Otras URLs de tu aplicación
]