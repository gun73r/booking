from app.models import Owner, Customer
from django.http import HttpResponse


def owner_required(view_func):
    def wrapper(request, *args, **kwargs):
        if isinstance(request.user, Owner):
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse(status=403)
    return wrapper


def customer_required(view_func):
    def wrapper(request, *args, **kwargs):
        if isinstance(request.user, Customer):
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse(status=403)
    return wrapper
