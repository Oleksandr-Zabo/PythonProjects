from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_crismastree_list, name='new_crismastree_list'),
    path('tree/<int:id>/', views.cristmas_tree_details, name='cristmas_tree_details'),
    path('like/<int:id>/', views.like_crismastree, name='like_crismastree'),
    path('winner/', views.winner_crismastree, name='winner_crismastree'),
]
