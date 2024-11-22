from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin
from . managers import UserManager
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver  # new
# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(
        _("phone_number"),
        max_length=11,
        unique=True,
        help_text=_(
            "Required. 11 numbers"
        ),
        error_messages={
            "unique": _("A user with that phone_number already exists."),
        },
    )
    email=models.EmailField(_("email address"),blank=True,unique=True,null=True)
    age=models.PositiveIntegerField(blank=True,null=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    objects = UserManager()
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    USERNAME_FIELD = "phone_number"
    
    def get_full_name(self):
        
        full_name = "%s %s" % (self.first_name , self.last_name)
        return full_name.strip()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

  


