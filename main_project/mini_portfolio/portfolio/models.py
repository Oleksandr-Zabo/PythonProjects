from django.db import models
from django.contrib.auth.models import User

# to create post (project)
class Project(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="portfolio_images/", blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.author.username})"



# to delete post (project)
class DeleteRequest(models.Model):
    STATUS_CHOICES = [
        ("pending", "Очікує"),
        ("approved", "Схвалено"),
        ("rejected", "Відхилено"),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="delete_requests")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"Запит на видалення {self.project.title} від {self.user.username}"


# User + telegram_id
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.username

