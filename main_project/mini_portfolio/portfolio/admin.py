from django.contrib import admin
from .models import Project, DeleteRequest

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    search_fields = ("title", "author__username")
    list_filter = ("created_at",)

@admin.register(DeleteRequest)
class DeleteRequestAdmin(admin.ModelAdmin):
    list_display = ("project", "user", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("project__title", "user__username")
