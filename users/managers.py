from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomManager(BaseUserManager):

    def create_user(self, email, password, **extras):
        if not email:
            raise ValueError(_("Email is a mandatory field"))

        email = self.normalize_email(email)
        user = self.model(email=email, **extras)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extras):
        extras.setdefault("is_staff", True)
        extras.setdefault("is_active", True)
        extras.setdefault("is_superuser", True)

        if "is_superuser" not in extras:
            raise ValueError(_("'is_superuser' is mandatory for superuser"))
        if "is_staff" not in extras:
            raise ValueError(_("'is_staff' is mandatory for superuser"))

        return self.create_user(email, password, **extras)
