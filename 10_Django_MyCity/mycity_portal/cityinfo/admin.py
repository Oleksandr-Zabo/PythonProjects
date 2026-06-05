from django.contrib import admin

from .models import Gallery, News


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active", "order", "uploaded_at"]
    list_editable = ["is_active", "order"]
    list_filter = ["is_active", "uploaded_at"]
    search_fields = ["title", "description"]
    readonly_fields = ["uploaded_at"]


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "is_published", "created_at"]
    list_editable = ["is_published"]
    list_filter = ["is_published", "created_at"]
    search_fields = ["title", "content"]
    readonly_fields = ["created_at", "updated_at"]

