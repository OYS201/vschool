from django.db import models
from django.contrib.auth import get_user_model
import functools
from django.shortcuts import redirect
from django.contrib import messages


def staff_authentication_required(view_func, redirect_url="teacher:login"):
    """
        this decorator ensures that a user is not logged in,
        if a user is logged in, the user will get redirected to 
        the url whose view name was passed to the redirect_url parameter
    """
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated and request.user.is_staff:
            return view_func(request,*args, **kwargs)
        messages.info(request, "You need to be logged out")
        print("You need to be logged out")
        return redirect(redirect_url)
    return wrapper

# def verification_required(view_func, verification_url="accounts:activate_email"):
#     """
#         this decorator restricts users who have not been verified
#         from accessing the view function passed as it argument and
#         redirect the user to page where their account can be activated
#     """
#     @functools.wraps(view_func)
#     def wrapper(request, *args, **kwargs):
#         if request.user.is_active:
#             return view_func(request, *args, **kwargs)
#         messages.info(request, "Email verification required")
#         print("You need to be logged out")
#         return redirect(verification_url)  
#     return wrapper


