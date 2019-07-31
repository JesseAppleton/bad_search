from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from .models import *

# Create your views here.
def index(request):
    return render(request, "index.html")

def search(request):
    if request.method == 'POST':
        search = request.POST["search_input"][0]
        word = get_random_string(length=4)
    return redirect(f"https://www.google.com/search?safe=off&source=hp&ei=WA1BXbWJB6eB5wKlmovoDQ&q={search}{word}")

def real_search(request):
    if request.method == 'POST':
        search = request.POST["search_input"]
        print(search)
    return redirect(f"https://lmgtfy.com/?q={search}")

''' TO DO:
        make words related to the first letter and reference them at random
        make real_search work correctly
            second modal based on the bottom of the screen?
                footer for bootstrap
        finish styling