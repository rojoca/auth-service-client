import bcrypt
from django.db import IntegrityError
from django.contrib.auth.hashers import check_password, make_password
from credentials.models import Credential


class BadCredentialValue(Exception):
    pass


def create_credential(username, password):
    if len(username) < 1:
        raise BadCredentialValue("No username")
    if len(password) < 1:
        raise BadCredentialValue("No password")
    try:
        credential = Credential(username=username)
        credential.password_hash = make_password(password, bcrypt.gensalt())
        credential.save()
    except IntegrityError:
        raise BadCredentialValue("Username cannot be registered")
    return credential


def check_credentials(username, password):
    creds = Credential.objects.filter(username=username)
    return len(creds) > 0 and check_password(password, creds[0].password_hash)
