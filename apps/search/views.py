from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def search(request):
    if request.method == 'POST':
        search = request.form["real_search"]
    return redirect(f"https://www.google.com/search?safe=off&source=hp&ei=WA1BXbWJB6eB5wKlmovoDQ&q={search}")

def real_search(request):
    if request.method == 'POST':
        search = request.form["real_search"]
    return redirect(f"https://lmgtfy.com/?q={search}")