from django.urls import path
from . import views

urlpatterns = [
    # Main routing views (Tasks 1-5)
    path('', views.home, name='home'),
    path('writers/', views.writer_list, name='writer_list'),
    path('writers/<slug:writer_slug>/', views.writer_detail, name='writer_detail'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:rating>/', views.book_detail_by_rating, name='book_detail_by_rating'),
    path('writers/<slug:writer_slug>/<slug:book_slug>/', views.book_detail_by_writer_and_slug, name='book_detail_by_writer_and_slug'),
    
    # Author CRUD operations
    path('authors/create/', views.AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/update/', views.AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author_delete'),
    
    # Book CRUD operations
    path('books/create/', views.BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
]