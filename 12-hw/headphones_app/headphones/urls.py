from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_model, name='show_model'),
]
