# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

# Personalizar la vista del modelo UserProfile
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Perfil del usuario'
    fk_name = 'user'
    fields = ('tipo_usuario', 'especialidad', 'telefono', 'ciudad', 'comuna')

# Función para obtener 'tipo_usuario' desde el perfil
def get_tipo_usuario(obj):
    return obj.profile.tipo_usuario if hasattr(obj, 'profile') else '-'
get_tipo_usuario.short_description = 'Tipo de usuario'

# Personalizar la vista del modelo User
class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)  # Esto incluye el perfil en la vista del usuario
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', get_tipo_usuario)
    list_filter = ('is_staff', 'is_superuser', 'groups')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

# Registra el modelo User y personaliza su vista
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Registrar el modelo UserProfile por separado si quieres verlo también en el admin
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'tipo_usuario', 'especialidad', 'telefono', 'ciudad', 'comuna')
    list_filter = ('tipo_usuario', 'especialidad')
    search_fields = ('user__username', 'user__email', 'telefono', 'ciudad')
