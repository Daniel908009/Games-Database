from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
    path('reviews/<int:pk>/delete/', views.delete_review, name='review_delete'),
    path('games/<int:pk>/', views.game_detail, name='game_detail'),
    path('studios/', views.studios, name='studios'),
    path('studios/<int:pk>/', views.studio_detail, name='studio_detail'),
    path('users/<str:username>/', views.user_profile, name='user_profile'),
    path('search/', views.search, name='search'),
]
