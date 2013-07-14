auth-service-client
===================

Authenticate service and python client. A django app provides two endpoints for
an authentication service that registers username/password combinations and
authenticates them:

    # to register
    POST /register
    username=yellow&password=password1

    # to authenticate
    POST /register
    username=yellow&password=password1

Invalid credentials will return status 400 responses.

The python client wraps http calls to this service with a simple interface. The
[requests](http://docs.python-requests.org/en/latest/) library is used for http
communication. The base URL for the service can be set as an environment
variable `AUTHENTICATE_URL` or added as a named argument to the client methods.

    import auth_client

    # to register
    auth_client.register("username", "password")

    # to authenticate
    auth_client.authenticate("username", "password")

    # when no url environment variable
    auth_client.authenticate("username", "password", url="http://127.0.0.1:8000")
