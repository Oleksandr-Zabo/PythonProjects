from django.urls import path

from feachers import views

urlpatterns = [
    path("", views.current_datetime_view, name="current_datetime"),
    path("table/", views.multiplication_table_view, name="multiplication_table"),
    path("programmer-day/", views.programmer_day_view, name="programmer_day"),
]

