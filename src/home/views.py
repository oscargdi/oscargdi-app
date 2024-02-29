from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render

from .forms import MessageForm
from .services import send_message


@login_required
def home(request: HttpRequest):
    if request.method == "GET":
        form = MessageForm()
        return render(request, "home/index.html", {"form": form})

    elif request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            message = form.cleaned_data["message"]
            send_message(title, message)
            return HttpResponseRedirect("/")


@login_required
def profile(request):
    return render(request, "home/profile.html")
