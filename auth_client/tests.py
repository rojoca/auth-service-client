import unittest2 as unittest
import requests
import auth_client
from mock import patch


@patch.object(requests, 'post')
class AuthClientTest(unittest.TestCase):
    def test_register_bad_scheme_raises_exception(self, post):
        with self.assertRaises(auth_client.BadUrlException):
            auth_client.register("yellow", "password", "www.google.com")
        with self.assertRaises(auth_client.BadUrlException):
            auth_client.register("yellow", "password", "fpt://www.google.com")

    def test_register_bad_domain_raises_exception(self, post):
        with self.assertRaises(auth_client.BadUrlException):
            auth_client.register("yellow", "password", "www.google")

    def test_register_bad_username_raises_exception(self, post):
        post.return_value.status_code = 400
        post.return_value.text = "Bad username or password"
        with self.assertRaises(auth_client.BadCredentialsException):
            auth_client.register("", "password")

    def test_register_bad_password_raises_exception(self, post):
        post.return_value.status_code = 400
        post.return_value.text = "Bad username or password"
        with self.assertRaises(auth_client.BadCredentialsException):
            auth_client.register("yellow", "")

    def test_register_bad_password_raises_exception(self, post):
        post.return_value.status_code = 400
        post.return_value.text = "Bad username or password"
        with self.assertRaises(auth_client.BadCredentialsException):
            auth_client.register("yellow", "")

    def test_register_successful_returns_true(self, post):
        post.return_value.status_code = 200
        post.return_value.text = "OK"
        self.assertTrue(auth_client.register("yellow", "password"))

    def test_register_raises_exception_if_message_not_ok(self, post):
        post.return_value.status_code = 200
        post.return_value.text = "FAIL"
        with self.assertRaises(auth_client.AuthServiceException):
            auth_client.register("yellow", "password")

    def test_register_raises_exception_if_status_500(self, post):
        post.return_value.status_code = 500
        post.return_value.text = "OK"
        with self.assertRaises(auth_client.AuthServiceException):
            auth_client.register("yellow", "password")

    def test_authenticate_bad_scheme_raises_exception(self, post):
        with self.assertRaises(auth_client.BadUrlException):
            auth_client.authenticate("yellow", "password", "www.google.com")
        with self.assertRaises(auth_client.BadUrlException):
            auth_client.authenticate("yellow", "password", "ftp://google.com")

    def test_authenticate_bad_domain_raises_exception(self, post):
        with self.assertRaises(auth_client.BadUrlException):
            auth_client.authenticate("yellow", "password", "www.google")

    def test_authenticate_fails_with_bad_username(self, post):
        post.return_value.status_code = 400
        post.return_value.text = "Bad username or password"
        with self.assertRaises(auth_client.BadCredentialsException):
            auth_client.authenticate("", "password")

    def test_authenticate_fails_with_bad_password(self, post):
        post.return_value.status_code = 400
        post.return_value.text = "Bad username or password"
        with self.assertRaises(auth_client.BadCredentialsException):
            auth_client.authenticate("yellow", "")

    def test_authenticate_successful_returns_true(self, post):
        post.return_value.status_code = 200
        post.return_value.text = "OK"
        self.assertTrue(auth_client.authenticate("yellow", "password"))

    def test_authenticate_raises_exception_if_message_not_ok(self, post):
        post.return_value.status_code = 200
        post.return_value.text = "OK"
        self.assertTrue(auth_client.authenticate("yellow", "password"))

    def test_authenticate_raises_exception_if_status_500(self, post):
        post.return_value.status_code = 500
        post.return_value.text = "OK"
        with self.assertRaises(auth_client.AuthServiceException):
            auth_client.register("yellow", "password")


if __name__ == '__main__':
    unittest.main()
