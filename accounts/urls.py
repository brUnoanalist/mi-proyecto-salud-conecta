# accounts/urls.py
from django.urls import path
from .views import (RegisterView, LoginView,EspecialidadesListView,UserProfileView)

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('especialidades/', EspecialidadesListView.as_view(), name='especialidades-list'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    
]
