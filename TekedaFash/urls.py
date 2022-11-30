from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Cliente.urls')),
    path('dashboard/', include('Administrador.urls')),
    path('dashboard/compras/', include('Compras.urls')),
    path('dashboard/ventas/', include('Ventas.urls')),
    path('dashboard/reporte/', include('Reporte.urls')),
    path('', include('pwa.urls')),
    path('google1bb11a63b6178071.html/', views.GoogleSearchConsoleView.as_view(), name='GoogleSearchConsole'),
]
