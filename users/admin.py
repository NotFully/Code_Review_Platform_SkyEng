from django.contrib import admin
from .models import User
from .forms import AdminUserRegistrationForm


class CustomUserAdmin(admin.ModelAdmin):

    form = AdminUserRegistrationForm
    model = User
    list_display_links = ("email",)
    list_display = ("email", "is_superuser")


admin.site.register(User, CustomUserAdmin)
