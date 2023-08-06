from django.contrib.auth import get_user_model
from django.conf import settings


User = get_user_model()

if hasattr(settings, "CHEDIDS_CONFS"):
    ACCOUNT_MODEL = settings.CHEDIDS_CONFS["PROFILE_MODEL"] or User
    TOKEN_EXPIRATION = settings.CHEDIDS_CONFS["TOKEN_EXPIRATION"] or 21600
else:
    ACCOUNT_MODEL = User
    TOKEN_EXPIRATION = 21600