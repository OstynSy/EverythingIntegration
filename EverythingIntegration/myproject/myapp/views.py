from django.shortcuts import render
from django.http import HttpResponse
from .NBGAPI import NBGIntegration, oauth_redirect
from notion_client import Client


def home(request):
    return HttpResponse("Hello, World!")
# Create your views here.

from django.shortcuts import redirect

def notion_auth(request):

    # Generate the authorization URL
    auth_url = "https://api.notion.com/v1/oauth/authorize?client_id=14df4f07-340d-43ee-bce4-d01b02e8441f&response_type=code&owner=user&redirect_uri=https%3A%2F%2F127.0.0.1%3A8000"

    # Redirect the user to the authorization URL
    return redirect(auth_url)
from pathlib import Path
def notion_callback(request):
    # Retrieve the authorization code from the query string
    auth_code = request.GET.get('code')
    print(auth_code)
    # Render a success page with the auth code and database ID
    return render(request, 'oauth_success.html', {'auth_code': auth_code})