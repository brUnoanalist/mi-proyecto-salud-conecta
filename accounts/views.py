
# Registro de usuario
# accounts/views.py
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer,UserProfileSerializer,EspecialidadSerializer
from .models import UserProfile
from rest_framework.permissions import IsAuthenticated




# Registro de usuario
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print("Datos recibidos:", request.data)  # Debug: Verifica los datos que llegan
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Errores en la validación:", serializer.errors)  # Debug: Verifica los errores
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Generación de tokens para el login
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        # Autenticación del usuario
        user = authenticate(username=username, password=password)

        if user is not None:
            # Obtener o crear un token de autenticación
            token, created = Token.objects.get_or_create(user=user)
            profile = UserProfile.objects.get(user=user) 

            # Responder con el token y el nombre de usuario
            return Response({
                "token": token.key,
                "username": user.username, # Incluyendo el username en la respuesta
                'email': user.email,
                'especialidad': profile.especialidad,
                'tipo_usuario': profile.tipo_usuario,
                'telefono': profile.telefono,
                'ciudad': profile.ciudad,
                'comuna': profile.comuna
                
            }, status=status.HTTP_200_OK)
        else:
            # Si las credenciales son incorrectas
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class EspecialidadesListView(APIView):
    def get(self, request):
        especialidades = UserProfile.ESPECIALIDADES_CHOICES
        serialized = EspecialidadSerializer(
            [{'value': value, 'label': label} for value, label in especialidades], many=True)
        return Response(serialized.data)
    

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.is_authenticated:
            try:
                user_profile = UserProfile.objects.get(user=request.user)
                print(f'Perfil encontrado: {user_profile}')
                return Response({
                    'nombre': request.user.username,
                    'email': request.user.email,
                    'especialidad': user_profile.especialidad,  # Accediendo a través del perfil de usuario
                    'tipo_usuario': user_profile.tipo_usuario,  # Accediendo a través del perfil de usuario
                    'telefono': user_profile.telefono or 'No disponible',  # Teléfono
                    'ciudad': user_profile.ciudad or 'No disponible',  # Ciudad
                    'comuna': user_profile.comuna or 'No disponible', 
                })
            except UserProfile.DoesNotExist:
                return Response({"detail": "User profile not found."}, status=404)
        else:
            return Response({"detail": "User not authenticated"}, status=401)