from django.contrib import admin
# Alias because we want our custom user to be called "UserAdmin"
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Common internationalization shorthand
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["email", "name"]
    fieldsets = (
        # Tuple containing UI section title (in this case no title) and fields
        (None, {"fields": ("email", "password")}),
        (
            _("Permissions"),
            {"fields": ("is_active", "is_staff", "is_superuser")},
        ),
        # "last_login" trailing comma to be recognized as a tuple
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    readonly_fields = ["last_login"]
    add_fieldsets = (
        (None, {
            "classes": ("wide",),  # This is an UI class modifier
            "fields": (
                "email",
                "password1",
                "password2",
                "name",
                "is_active",
                "is_staff",
                "is_superuser",
            )
        }),
    )


admin.site.register(models.User, UserAdmin)
