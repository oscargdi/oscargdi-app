from django.http import HttpRequest
from django.shortcuts import render

from . import models


def index(request: HttpRequest):
    accounts = models.Account.objects.filter(user=request.user)
    return render(request, "finance/index.html", context={"accounts": accounts})
