from django.urls import path
from . import views
urlpatterns = [
    path('health/', views.home, name="health"),
    path('register/', views.register, name="register"),
    path(r'profile/(?P<pk>\w+)/$', views.profile, name="profile"),
    path(r'change-password/(?P<pk>\w+)/$', views.password_changer, name="password_changer")
]
