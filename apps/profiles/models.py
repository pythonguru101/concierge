from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe
from django.core.files.storage import default_storage
from django.core.validators import RegexValidator


class User(AbstractUser):
    username = models.CharField(_('User name'), max_length=255, null=True, blank=True, unique=True)
    first_name = models.CharField(_('First Name'), max_length=255, null=True, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=255, null=True, blank=True)
    # phone_number = PhoneNumberField(_('Phone Number'), null=True, blank=True, unique=True)
    phone_regex = RegexValidator(regex=r'^[2-9]\d{2}-\d{3}-\d{4}$',
                                 message="Phone number must be entered in the format: 'xxx-xxx-xxxx'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    email = models.EmailField(_('Email'), max_length=255, null=True, blank=True)
    twitter = models.URLField(_('Twitter'), max_length=255, null=True, blank=True)
    instagram = models.URLField(_('Instagram'), max_length=255, null=True, blank=True)
    facebook = models.URLField(_('Facebook'), max_length=255, null=True, blank=True)

