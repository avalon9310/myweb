from django.shortcuts import render
from G import G
# Create your views here.
def html(request):
    info = G.saveHistory(request, 'home')
    request.session["currentPage"] = "/"
    return  render(request,"home.html",{"info": info[1],"userAccount":G.userAccount(request)})