import base64
from django.conf import settings

def checkAuth(request):
    auth = request.META['HTTP_AUTHORIZATION'].split()
    auth_pair = base64.b64decode(auth[1]).decode("utf-8").split(":")
    username = settings.WORKELECTION_WEBHOOK_USERNAME
    password = settings.WORKELECTION_WEBHOOK_PASSWORD
    return (auth_pair[0] == username and auth_pair[1] == password)