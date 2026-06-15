from django.urls import path
from . import views

urlpatterns = [
    path('prediction/', views.get_prediction, name='get_prediction'),
    path('random-number/', views.get_random_number, name='get_random_number'),
    path('random-range/<int:start>/<int:end>/', views.get_random_by_range, name='get_random_by_range'),
    path('random-numbers/<int:start>/<int:end>/<int:count>/', views.get_random_numbers, name='get_random_numbers'),
]
