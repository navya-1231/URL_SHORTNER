from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
import random, string

def generate_unique_code(length=6):
    while True:
        code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
        if not URL.objects.filter(short_url=code).exists():
            return code

def home(request):
    short_url = None
    error = None

    if request.method == "POST":
        long_url = request.POST.get("long_url")

        if long_url:
            code = generate_unique_code()
            URL.objects.create(long_url=long_url, short_url=code)
            short_url = request.build_absolute_uri('/') + code
        else:
            error = "Please enter a valid URL."

    return render(request, "home.html", {"short_url": short_url, "error": error})

def redirect_url(request, code):
    url = get_object_or_404(URL, short_url=code)
    return redirect(url.long_url)
