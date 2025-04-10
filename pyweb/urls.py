"""
URL configuration for pyweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#import first
from home import views as home #from home import views as home
import gallery.views as gallery
import travel.views as travel
import tools.views as tools
import twstock.views as twstock
import twgold.views as twgold
import solar.views as solar
import session.views as session
from django.conf import settings
from django.conf.urls.static import static
from upload import views as upload


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home.html),  # html 是函數名稱，不是副檔名
    path("gallery/", gallery.html),

    path("gallery/thumb/", gallery.thumb),
    path("gallery/thumb_doing/", gallery.thumb_doing),
    path("gallery/listThumbDir/", gallery.listThumbDir),

    path("travel/", travel.html),
    path("tools/", tools.html),
    path("twstock/", twstock.html),
    path("twgold/", twgold.html),
    path("login/", session.login),
    path("logout/", session.logout),
    path("login_process/", session.login_process),
    # path("check_session/", session.check_session),
    path("reject/", session.reject),
    path("solar/", solar.html),
    path("upload/photo_form/", upload.photo_form),
    path("upload/photo_process/", upload.photo_process),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
