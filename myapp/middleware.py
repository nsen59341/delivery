from django.contrib.auth import login, user_logged_in
from django.shortcuts import redirect

def auth(func):
    def inner_wrap(request, *args, **kwargs):
        # if user_logged_in:
        if request.user.is_authenticated==True:
            return func(request, *args, **kwargs)
        else:
            return redirect('login')
    return inner_wrap

def guest(func):
    def inner_wrap(request, *args, **kwargs):
        if request.user.is_authenticated==False:
            return func(request, *args, **kwargs)
        else:
            return redirect('index')
    return inner_wrap