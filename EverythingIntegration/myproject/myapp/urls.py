from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notion-auth/', views.notion_auth, name='notion-auth'),
    path('', views.notion_callback, name='notion-callback'),
]