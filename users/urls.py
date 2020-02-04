from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('logout/', views.logout, name = 'logout'),
    path('login/', views.login, name = 'login'),
    path('profile/<str:username>', views.profile, name = 'profile'),
    path('update/<int:id>', views.update, name = 'update'),
]
