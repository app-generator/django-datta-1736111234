# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    nickname = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Note(models.Model):

    #__Note_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(max_length=255, null=True, blank=True)
    create_at = models.IntegerField(null=True, blank=True)

    #__Note_FIELDS__END

    class Meta:
        verbose_name        = _("Note")
        verbose_name_plural = _("Note")


class Notemedia(models.Model):

    #__Notemedia_FIELDS__
    note_id = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)

    #__Notemedia_FIELDS__END

    class Meta:
        verbose_name        = _("Notemedia")
        verbose_name_plural = _("Notemedia")



#__MODELS__END
