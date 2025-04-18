from django.contrib import admin
# Alias because we want our custom user to be called "UserAdmin"
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["email", "name"]


admin.site.register(models.User, UserAdmin)
