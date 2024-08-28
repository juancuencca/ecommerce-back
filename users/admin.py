from django.contrib import admin
from .models import User

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ('email', 'name')
    ordering = ('email',)
    readonly_fields = ('date_joined', 'last_login')