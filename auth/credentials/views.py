from django.views.generic import View
from django.http import HttpResponse, HttpResponseBadRequest

from credentials import api


class CreateCredentialView(View):
    http_method_names = ['post', 'options']

    def post(self, request, *args, **kwargs):
        """
        Create a new username/password combination in the db
        """
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        try:
            api.create_credential(username, password)
        except api.BadCredentialValue as e:
            return HttpResponseBadRequest(e)
        else:
            return HttpResponse("OK")


class CheckCredentialsView(View):
    http_method_names = ['post', 'options']

    def post(self, request, *args, **kwargs):
        """
        Check a given username/password combination against
        the stored credentials. Return an OK message if
        successful otherwise return a 400 response
        """
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if api.check_credentials(username, password):
            return HttpResponse("OK")

        # bad username or password
        return HttpResponseBadRequest("Invalid username or password")
