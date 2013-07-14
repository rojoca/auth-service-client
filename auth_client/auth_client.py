import os
import requests
import urlparse


DEFAULT_URL = os.getenv('AUTHENTICATE_URL', "http://127.0.0.1:8000")


class BadUrlException(Exception):
    pass


class BadCredentialsException(ValueError):
    """
    Indicates there is a problem with provided credentials
    """
    pass


class AuthServiceException(Exception):
    """
    Indicates there is a problem with the service
    """
    pass


def register(username, password, url=DEFAULT_URL):
    return _request('register', username, password, url=url)


def authenticate(username, password, url=DEFAULT_URL):
    return _request('authenticate', username, password, url=url)


def _request(method, username, password, url=DEFAULT_URL):
    _validate_url(url)
    payload = {'username': username, 'password': password}
    r = requests.post("%s/%s" % (url,  method), data=payload)
    if r.status_code == 400:
        raise BadCredentialsException(r.text)
    if r.status_code != 200 or r.text != 'OK':
        raise AuthServiceException(r.text)
    return True


def _validate_url(url):
    o = urlparse.urlparse(url)
    if o.scheme != "http" or not o.netloc:
        raise BadUrlException("URL must be http")
