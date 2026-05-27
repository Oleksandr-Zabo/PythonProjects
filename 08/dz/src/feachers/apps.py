from django.apps import AppConfig

# Django сам шукає шаблони в templates/ всередині кожного app. Тому ми можемо просто створити папку templates/ всередині feachers/ і помістити туди наші HTML файли.
class FeachersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "feachers"

