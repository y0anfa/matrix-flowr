from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if request.GET.get('next') is not None:
                return HttpResponseRedirect(request.GET.get('next'))
            return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect('/')

    else:
        return render(request, "authentication/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/auth/login')
