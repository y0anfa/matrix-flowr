from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from urllib.parse import urlparse

ALLOWED_DOMAINS = ["127.0.0.1"]

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            url = request.GET.get('next')

            if url is not None:
                parsed_url = urlparse(url)
                if parsed_url.netloc in ALLOWED_DOMAINS:
                    return HttpResponseRedirect('http://' + parsed_url.netloc)
            return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect('/')

    else:
        return render(request, "authentication/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/auth/login')
