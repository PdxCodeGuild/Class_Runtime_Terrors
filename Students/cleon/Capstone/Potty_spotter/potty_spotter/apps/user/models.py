from django.contrib.auth.models import AbstractUser, UserManager as AbstractUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(AbstractUserManager):
    pass


class User(AbstractUser):
    name = models.CharField(_("Name"), blank=True, max_length=255)

    USERNAME_FIELD = "username"

    class Types(models.IntegerChoices):
        SYS_ADMIN = 1, _("System Admin")
        GEN_USER = 2, _("General User")

    base_type = Types.GEN_USER
    type = models.IntegerField(
        _("Type"), choices=Types.choices, default=base_type)

    class ThemeOptions(models.TextChoices):
        THEME_LIGHT = "light", _("Light")
        THEME_DARK = "dark", _("Dark")

    css_theme_preference = models.CharField(
        max_length=20, default=ThemeOptions.THEME_DARK, choices=ThemeOptions.choices
    )

    objects = UserManager()

    @property
    def is_sysadmin(self):
        if self.type == self.Types.SYS_ADMIN:
            return True
        return False

    @property
    def is_general_user(self):
        if self.type == self.Types.GEN_USER:
            return True
        return False


class SysAdminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(
            *args, **kwargs).filter(type=User.Types.SYS_ADMIN)


class GeneralUserManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(
            *args, **kwargs).filter(type=User.Types.GEN_USER)


class SysAdmin(User):
    """
    Sysadmin users
    """

    base_type = User.Types.SYS_ADMIN
    objects = SysAdminManager()

    class Meta:
        proxy = True


class GeneralUser(User):
    """
    General users
    """

    base_type = User.Types.GEN_USER
    objects = GeneralUserManager()

    class Meta:
        proxy = True
