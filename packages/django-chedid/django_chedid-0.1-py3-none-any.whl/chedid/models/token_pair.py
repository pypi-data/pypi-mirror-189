"""
This file defines the model of TokenPair and its own workflow.
"""

from django.db import models
from django.utils import timezone
from .. app_setup import *

import uuid


def gen_token():
    """
    A function to gen a UUID4 token that is unic on database

    :return: UUID4 object
    """

    new_token = uuid.uuid4()
    while TokenPair.objects.filter(auth_token=new_token) or TokenPair.objects.filter(recovery_token=new_token):
        new_token = uuid.uuid4()
    return new_token


class TokenPair(models.Model):
    """
    This model is the authentication data
    """
    created_at = models.DateTimeField(auto_now_add=True)
    auth_token = models.UUIDField(unique=True)
    recovery_token = models.UUIDField(unique=True)
    valid = models.BooleanField(default=True)
    profile = models.ForeignKey(ACCOUNT_MODEL, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.auth_token = gen_token()
        self.recovery_token = gen_token()
        models.ForeignKey
        return super().save(force_insert, force_update, using, update_fields)

    def is_valid(self):
        self.valid = ((timezone.now().timestamp() - self.created_at.timestamp()) < TOKEN_EXPIRATION)
        super().save()
        return self.valid
