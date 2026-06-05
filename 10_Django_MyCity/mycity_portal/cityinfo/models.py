from django.db import models


class Gallery(models.Model):
    """Local image gallery for the city portal"""
    title = models.CharField(max_length=200, verbose_name="Назва")
    description = models.TextField(blank=True, verbose_name="Опис")
    image = models.ImageField(upload_to="gallery/", verbose_name="Зображення")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Завантажено")
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Галереї"
        verbose_name_plural = "Галереї"
        ordering = ["order", "-uploaded_at"]

    def __str__(self):
        return self.title


class News(models.Model):
    """Local news for the city portal"""
    title = models.CharField(max_length=300, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Зміст")
    image = models.ImageField(upload_to="news/", blank=True, null=True, verbose_name="Зображення")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено")
    is_published = models.BooleanField(default=True, verbose_name="Опубліковано")

    class Meta:
        verbose_name = "Новина"
        verbose_name_plural = "Новини"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

