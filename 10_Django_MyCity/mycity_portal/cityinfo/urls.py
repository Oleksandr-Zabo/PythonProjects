from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),

    # News - accept optional extra path and route to same view
    path("news/", views.news, name="news"),
    path("news/<path:extra>/", views.news, name="news_extra"),

    # Management / staff
    path("management/", views.management, name="management"),
    path("management/<path:extra>/", views.management, name="management_extra"),

    # Facts and landmarks
    path("facts/", views.facts, name="facts"),
    path("facts/<path:extra>/", views.facts, name="facts_extra"),

    # Landmarks (видатне місто)
    path("landmarks/", views.landmarks, name="landmarks"),
    path("landmarks/<path:extra>/", views.landmarks, name="landmarks_extra"),

    # Notable people (видатні люди)
    path("people/", views.people, name="people"),
    path("people/<path:extra>/", views.people, name="people_extra"),

    # Photo album
    path("photos/", views.photos, name="photos"),
    path("photos/<path:extra>/", views.photos, name="photos_extra"),

    # History section
    path("history/", views.history, name="history"),
    path("history/people/", views.history_people, name="history_people"),
    path("history/photos/", views.history_photos, name="history_photos"),
    path("history/<path:extra>/", views.history, name="history_extra"),

    # Contact phones
    path("services/", views.services, name="services"),
    path("services/<path:extra>/", views.services, name="services_extra"),

    # Gallery from database
    path("gallery/", views.gallery_db, name="gallery_db"),
    path("gallery/<path:extra>/", views.gallery_db, name="gallery_db_extra"),
]



