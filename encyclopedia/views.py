import random

from django.shortcuts import render, redirect

from . import util


def index(request):
    if request.GET.get("q", None):
        result = util.search_entry(request.GET["q"])
        if len(result) == 1:            
            return redirect("page", title=result[0])
        else:
            return render(request, "encyclopedia/index.html", {
                "entries": result
            })
    
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, title):    
    return render(request, "encyclopedia/page.html", {
        "entries": util.mdconvert(util.get_entry(title)),
        "title": title
    })

def save(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["entry"]
        if util.get_entry(title):
            return render(request, "encyclopedia/save.html", {
                "error": f"{title} already exist in wiki"
            })
        else:
            util.save_entry(title, content)
        
        return redirect('page', name=title)
        
    else:
        return render(request, "encyclopedia/save.html")


def random_page(request):
    return redirect("page", title=random.choice(util.list_entries())) 


def edit(request, title):
    if request.method == "POST":
        content = request.POST["entry"]
        util.save_entry(title, content)
        return redirect("page", title)
    else:
        entry = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "entry": entry
        })
