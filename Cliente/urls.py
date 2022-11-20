from django.urls import path
from django.contrib.auth import views as auth_vistas
from . import views

urlpatterns = [
    path('', views.index, name = "inicio"),
    path('iniciarSesion', views.iniciarSesion, name = "iniciarSesion"),
    path('cerrarSesion', views.cerrarSesion, name = "cerrarSesion"),
    
    #Reestablecer contraseña
    path('reestablecerContraseña', auth_vistas.PasswordResetView.as_view(template_name = "Cliente/reestablecerContraseña/reestablecerContraseña.html"), name = "password_reset"),
    path('reestablecerContraseñaEnviado', auth_vistas.PasswordResetDoneView.as_view(template_name = "Cliente/reestablecerContraseña/reestablecerContraseñaEnviado.html"), name = "password_reset_done"),
    path('establecerContraseña/<uidb64>/<token>/', auth_vistas.PasswordResetConfirmView.as_view(template_name = "Cliente/reestablecerContraseña/establecerContraseñaNueva.html"), name = "password_reset_confirm"),
    path('contraseñaEstablecida', auth_vistas.PasswordResetCompleteView.as_view(template_name = "Cliente/reestablecerContraseña/reestablecerContraseñaCompletado.html"), name = "password_reset_complete"),
    #Mis Compras
    path('misCompras', views.misCompras, name = "misCompras"),
    path('detalledemiCompra/<id>', views.detalledemiCompra, name = "detalledemiCompra"),
    #------------
    path('registrarse/', views.registrarse),
    path('registrarUsuario', views.regisUsuario,),
    #------------
    path('productos/', views.productos),

    #----------
    path('productos/detalles/<int:id>', views.detalleProducto)
]