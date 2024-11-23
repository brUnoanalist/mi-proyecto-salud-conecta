# accounts/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile
from rest_framework.response import Response

from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['tipo_usuario', 'especialidad', 'telefono', 'ciudad', 'comuna']

    def validate(self, data):
        tipo_usuario = data.get('tipo_usuario')

        # Si el tipo de usuario es 'paciente', la especialidad no debe ser requerida
        if tipo_usuario == 'paciente' and data.get('especialidad'):
            raise serializers.ValidationError({'especialidad': 'Los pacientes no tienen especialidad.'})

        # Si el tipo de usuario no es 'profesional', la especialidad debe ser None
        if tipo_usuario != 'profesional':
            data['especialidad'] = None  # Asegurarse de que 'especialidad' sea None si no es profesional

        return data

class RegisterSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile']

    def create(self, validated_data):
        # Extraer el perfil y quitarlo de los datos del usuario
        profile_data = validated_data.pop('profile')
        
        # Crear el usuario
        user = User.objects.create_user(**validated_data)
        
        # Crear el perfil de usuario
        UserProfile.objects.create(user=user, **profile_data)
        
        return user
 
class EspecialidadSerializer(serializers.Serializer):
    value = serializers.CharField()
    label = serializers.CharField()

