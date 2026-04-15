from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.shortcuts import render, redirect

def login_view(request):
	return render(request, 'accounts/login.html')

def bienvenido_view(request):
	return render(request, 'accounts/bienvenido.html')

@api_view(['GET'])
def login_api(request):
    username = request.GET.get('user')
    password = request.GET.get('pass')
    if not username or not password:
        return Response({'error': 'Usuario y contraseña requeridos.'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.get(user=username, pass_field=password)
        return Response({'success': True, 'message': 'Login correcto'}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'success': False, 'error': 'Usuario o contraseña incorrectos.'}, status=status.HTTP_401_UNAUTHORIZED)
