from django.contrib import admin
from .models import TodoItem, SignUpData

admin.site.register(TodoItem)

@admin.register(SignUpData)
class SignUpDataAdmin(admin.ModelAdmin):
    list_display = ('username',)
