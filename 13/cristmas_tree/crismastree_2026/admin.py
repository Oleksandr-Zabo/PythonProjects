from django.contrib import admin
from .models import Crismastree

@admin.register(Crismastree)
class CrismastreeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_by', 'created_at', 'likes_count')
    search_fields = ('name', 'description')
