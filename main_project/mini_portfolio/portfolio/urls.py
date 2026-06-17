from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("projects/", views.project_list, name="project_list"),
    path("projects/add/", views.add_project, name="add_project"),
    path("projects/<int:pk>/", views.project_detail, name="project_detail"),
    path("projects/<int:project_id>/delete_request/", views.delete_request_view, name="delete_request"),
    path("connect-telegram/", views.connect_telegram, name="connect_telegram"),
]
