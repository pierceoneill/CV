"""pierceoneillcv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path as url
from django.conf.urls import include
from django.views.generic import RedirectView
from django.contrib import admin
from home.views import get_index
from blog.views import PostListView
from accounts import urls as urls_accounts
from accounts import url_reset
from blog import urls as urls_blog
from django.views import static
from django.contrib.auth import views
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^$', get_index, name='index'),
    url(r'^blog/', include(urls_blog)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
 ]   