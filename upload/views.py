import os.path
import platform
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from G import G
# Create your views here.

def photo_form(request):
    info = G.saveHistory(request, '準備上傳圖片')
    request.session["currentPage"] = "/upload/photo_form"
    if 'userAccount' not in request.session:
        return redirect("/login")

    return render(request, "upload/photo_form.html", {"state":"first","info":info[1],"userAccount":G.userAccount(request)})


def photo_process(request):
    info = G.saveHistory(request, '上傳成功')
    if platform.system()=="Linux":
        root="/data/upload"
    else:
        root="C:/upload/primitive"

    current=datetime.now()
    yyyy=current.strftime("%Y")
    ymd=current.strftime("%Y%m%d")
    path=os.path.join(root, yyyy, ymd)
    if not os.path.exists(path):
        os.makedirs(path)
        img=request.FILES["userFile"]
        fileName=os.path.join(path, str(img))
        with open(fileName, 'wb') as file:
            for data in img.chunks():
                file.write(data)

    return render(request, "upload/photo_form.html", {"state":"ok","info":info[1],"userAccount":G.userAccount(request)})
