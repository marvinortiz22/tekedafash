from django.http import HttpResponse
from django.shortcuts import render, redirect


def usuarioAutenticado(view_func):
    def wrapper_func(request,  *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def clienteAutenticado(view_func):
    def wrapper_func(request,  *args, **kwargs):
        if request.user.is_staff:
            return redirect('/dashboard')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def adminAutenticado(view_func):
    def wrapper_func(request,  *args, **kwargs):
        if request.user.is_staff == 0:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

