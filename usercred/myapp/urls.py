from django.urls import path
from . import views
urlpatterns = [
    path('health/', views.home, name="health"),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile")
]
