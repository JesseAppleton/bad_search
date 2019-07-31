from django.shortcuts import render, redirect
import random
import urllib.request

# Create your views here.
def index(request):
    return render(request, "index.html")
    
def real_search(request):
    search = "How to use google like a normal person"
    return redirect(f"https://lmgtfy.com/?q={search}")

def search(request):
    search_list = []
    if request.method == 'POST':
        search = request.POST["search_input"][0].lower()
        word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
        response = urllib.request.urlopen(word_url)
        long_txt = response.read().decode()
        for i in long_txt.splitlines():
            if i[0] == search:
                search_list.append(i)
        words = random.choice(search_list)
    return redirect(f"https://www.google.com/search?safe=off&source=hp&ei=WA1BXbWJB6eB5wKlmovoDQ&q={words}")