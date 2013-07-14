"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from credentials import api


class ApiTest(TestCase):
    def setUp(self):
        api.create_credential("yellow", "password1")
        api.create_credential("red", "password2")

    def test_cannot_create_credential_with_empty_username(self):
        with self.assertRaises(api.BadCredentialValue):
            api.create_credential("", "password1")

    def test_cannot_create_credential_with_empty_password(self):
        with self.assertRaises(api.BadCredentialValue):
            api.create_credential("yellow2", "")

    def test_cannot_create_credential_with_empty_username_and_password(self):
        with self.assertRaises(api.BadCredentialValue):
            api.create_credential("", "")

    def test_cannot_create_credential_with_existing_username(self):
        with self.assertRaises(api.BadCredentialValue):
            api.create_credential("yellow", "password2")

    def test_incorrect_username_returns_false(self):
        self.assertFalse(api.check_credentials("", "password1"))
        self.assertFalse(api.check_credentials("incorrect", "password1"))
        self.assertFalse(api.check_credentials("badyellow", "password1"))
        self.assertFalse(api.check_credentials("yellowbad", "password1"))

    def test_incorrect_password_returns_false(self):
        self.assertFalse(api.check_credentials("yellow", ""))
        self.assertFalse(api.check_credentials("yellow", "incorrect"))
        self.assertFalse(api.check_credentials("yellow", "badpassword1"))
        self.assertFalse(api.check_credentials("yellow", "password1bad"))

    def test_correct_credentials_return_true(self):
        self.assertTrue(api.check_credentials("yellow", "password1"))
        self.assertTrue(api.check_credentials("red", "password2"))
