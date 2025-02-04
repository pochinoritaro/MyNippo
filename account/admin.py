from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # 表示するフィールドをカスタマイズ（必要に応じて調整）
    list_display = ("id", "username", "email", "is_staff", "is_active", "icon", "last_login", "date_joined")
    search_fields = ("username", "email")
