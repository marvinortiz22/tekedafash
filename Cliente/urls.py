from django.urls import path
from django.contrib.auth import views as auth_vistas
from . import views

urlpatterns = [
    path('', views.index, name="inicio"),
    path('iniciarSesion', views.iniciarSesion, name="iniciarSesion"),
    path('cerrarSesion', views.cerrarSesion, name="cerrarSesion"),
    path('quienesSomos', views.quieneSomos, name="quienesSomos"),

    # Reestablecer contraseña
    path('reestablecerContraseña', auth_vistas.PasswordResetView.as_view(
        template_name="Cliente/reestablecerContraseña/reestablecerContraseña.html"), name="password_reset"),
    path('reestablecerContraseñaEnviado', auth_vistas.PasswordResetDoneView.as_view(
        template_name="Cliente/reestablecerContraseña/reestablecerContraseñaEnviado.html"), name="password_reset_done"),
    path('establecerContraseña/<uidb64>/<token>/', auth_vistas.PasswordResetConfirmView.as_view(
        template_name="Cliente/reestablecerContraseña/establecerContraseñaNueva.html"), name="password_reset_confirm"),
    path('contraseñaEstablecida', auth_vistas.PasswordResetCompleteView.as_view(
        template_name="Cliente/reestablecerContraseña/reestablecerContraseñaCompletado.html"), name="password_reset_complete"),
    # Mis Compras
    path('misCompras', views.misCompras, name="misCompras"),
    path('detalledemiCompra/<id>', views.detalledemiCompra,
         name="detalledemiCompra"),
    path('registrarOrden/', views.realizarOrden, name = "realizarOrden"),
    # Registro
    path('registrarse/', views.registrarse),
    path('registrarUsuario', views.regisUsuario,),

    # Productos
    path('productos/', views.productos, name="productos"),
    path('productos/detalles/<int:id>', views.detalleProducto, name="detalleDeProducto"),
    path('obtenerCantidadTalla/', views.obtenerCantidadTalla, name = 'obtenerCantidadTalla'),
    path('miCarrito', views.miCarrito, name="carrito"),
    path('agregarEnCarrito/<int:id>', views.agregarPrenda, name = "agregarPrenda"),
    path('quitarPrenda/<int:id>', views.quitarPrenda, name = 'quitarPrenda'),
    path('limpiarCarrito', views.limpiarCarrito, name = "limpiarCarrito"),
    path('buscar/', views.busqueda, name="buscar"),
    # ----------
    path('editarPerfil', views.editarPerfil, name="editar perfil"),
    path('Perfil/', views.Perfil, name="Perfil"),
    path('cambiarContraseña/', views.cambiarContraseña, name="cambiar contraseña"),
    
    

]
