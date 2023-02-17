from django.contrib import admin
from .models import TodoApp
# Register your models here.


@admin.register(TodoApp)
class TodoAppAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'text', 'created_at', 'updated_at']
