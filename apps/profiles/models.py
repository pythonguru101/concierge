from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe
from django.core.files.storage import default_storage

import django


class User(AbstractUser):
    photo = models.ImageField(_('Photo'), upload_to='userphotos/', null=True, blank=True)
    username = models.CharField(_('User name'), max_length=255, null=True, blank=True, unique=True)
    first_name = models.CharField(_('First Name'), max_length=255, null=True, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=255, null=True, blank=True)
    phone_number = models.CharField(_('Phone Number'), max_length=255, null=True, blank=True)
    email = models.CharField(_('Email'), max_length=255, null=True, blank=True)
    twitter = models.CharField(_('Twitter'), max_length=255, null=True, blank=True)
    instagram = models.CharField(_('Instagram'), max_length=255, null=True, blank=True)
    facebook = models.CharField(_('Facebook'), max_length=255, null=True, blank=True)

    @property
    def photo_url(self):
        if not self.photo:
            return ''

        if default_storage.exists(self.photo.path):
            return '%s%s' % (settings.MEDIA_URL, self.photo)
        else:
            return ''

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150"/>' % self.photo_url)

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
