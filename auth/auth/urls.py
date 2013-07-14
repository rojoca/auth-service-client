from django.conf.urls import patterns, url
from credentials.views import CreateCredentialView, CheckCredentialsView

urlpatterns = patterns(
    '',
    url(r'^register$', CreateCredentialView.as_view()),
    url(r'^authenticate$', CheckCredentialsView.as_view()),
)
