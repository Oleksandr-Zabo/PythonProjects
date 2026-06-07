from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    bio = models.TextField()
    birth_year = models.IntegerField()
    death_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    year = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField(default=0)  # Position in top books

    def __str__(self):
        return self.title
