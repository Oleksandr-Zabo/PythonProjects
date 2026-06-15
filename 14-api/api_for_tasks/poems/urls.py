from django.urls import path
from . import views

urlpatterns = [
    path('random/', views.random_poem, name='random_poem'),
    path('random/author/<int:author_id>/', views.random_poem_by_author, name='random_poem_by_author'),
    path('random/theme/<int:theme_id>/', views.random_poem_by_theme, name='random_poem_by_theme'),
    path('author/<int:author_id>/poems/', views.poems_by_author, name='poems_by_author'),
    path('authors/', views.all_authors, name='all_authors'),
    path('themes/', views.all_themes, name='all_themes'),
    path('theme/<int:theme_id>/poems/', views.poems_by_theme, name='poems_by_theme'),
]
