# MVT (model view template)

from django.shortcuts import render

def home_page(request):
    return render(request, "hello_world.html")

