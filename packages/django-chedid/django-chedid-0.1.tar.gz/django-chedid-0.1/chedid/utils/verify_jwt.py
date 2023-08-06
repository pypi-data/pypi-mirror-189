from django.apps import apps
from typing import Union
from jwt.exceptions import DecodeError
from .. app_setup import *

import base64
import jwt
import json


user_model = apps.get_model(ACCOUNT_MODEL)

def base64url_decoder(input: Union[str, bytes]) -> bytes:
    """
    This function pre-loads the input for the correct decode of urlsafe

    :param input: The bas64url encoded
    :return: the decoded input
    """

    if isinstance(input, str):
        input = input.encode("ascii")
    rem = len(input) % 4
    if rem > 0:
        input += b"=" * (4 - rem)
    return base64.urlsafe_b64decode(input)

def unpack_jwt(jwt_message: str, renew=False):
    """
    This is the main function do unpack a JWT message in this system

    :param jwt_message: the JWT gross message
    :param renew: the flag that indicate if it's a call of renew-tokens
    :return: the return consists in 5 parameters "found", "profile", "decoded", "key" and "bad_request"
        found: if has matched a profile and a TokenPair from this message
        profile: if found, returns the user model object from TokenPair. Else returns None
        decoded: if found, returns the decoded message as a Dictionary objects. Else None
        key: if found, the encryption key of message (to encrypt the response)
        bad_request: if important data is missing in message
    """

    found = False
    decoded = None
    key = None
    bad_request = False

    if type(jwt_message) != str or jwt_message.count(".") != 2:
        bad_request = True
        return found, None, decoded, key, bad_request

    header_gross, body_gross, signature_gross = jwt_message.split(".")
    body = json.loads(base64url_decoder(body_gross).decode("utf-8"))

    if "email" not in body.keys():
        bad_request = True
        return found, None, decoded, key, bad_request

    profile = user_model.objects.filter(user__email=body["email"]).first()
    if profile:
        if profile.active:
            for p_key in profile.tokenpair_set.all():
                p_key.is_valid()

            tokens = [tk for tk in profile.tokenpair_set.filter(valid=not renew)]


            found = False
            decoded = None

            for token in tokens:
                if not found:
                    try:
                        decoded = jwt.decode(jwt_message, str(token.auth_token), algorithms="HS256")
                        found = True
                        key = token.auth_token

                    except DecodeError:
                        pass
        else:
            profile = None
    else:
        profile = None
    return found, profile, decoded, str(key), bad_request


def pack_jwt(message: dict, key: str):
    """
    The responsible function to pack the JWT

    :param message: Dictionary data
    :param key: The same key from request
    :return: The encoded JWT
    """
    return jwt.encode(message, key, algorithm="HS256")


