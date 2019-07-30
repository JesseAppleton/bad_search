from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def search(request):
    return redirect("http://google.com")

def real_search(request):
    if request.method == 'POST':
        search = request.form["real_search"]
    return redirect(f"https://lmgtfy.com/?q={search}")