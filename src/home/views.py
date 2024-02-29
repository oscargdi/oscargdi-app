from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render

from .forms import MessageForm
from .tasks import async_send_message


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
            async_send_message.send_with_options(args=(title, message), delay=5000)
            return HttpResponseRedirect("/")


@login_required
def profile(request):
    return render(request, "home/profile.html")
