from django.shortcuts import render, redirect
from G import G

# Create your views here.

def html(request):
    info = G.saveHistory(request, 'twgold')
    request.session["currentPage"] = "/twgold"
    if 'userAccount' not in request.session:
        return redirect("/login")
    return render(request,'twgold.html',{"info": info[1],"userAccount":G.userAccount(request)})