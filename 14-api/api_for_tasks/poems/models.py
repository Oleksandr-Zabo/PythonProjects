from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Poem(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="poems")
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, related_name="poems")

    def __str__(self):
        return self.title
