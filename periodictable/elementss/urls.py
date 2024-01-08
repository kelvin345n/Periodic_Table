from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('description/<str:pk>', views.description, name='description'),
    path('unicorn/', include("django_unicorn.urls")),
]