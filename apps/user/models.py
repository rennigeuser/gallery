from django.db import models
from .manager import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext as _


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name=_('email address'),            
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Yes, always
        return True

    def has_module_perms(self, app_label):
        # Yes, always
        return True

    @property
    def is_staff(self):
        # All admins are staff
        return self.is_admin

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
