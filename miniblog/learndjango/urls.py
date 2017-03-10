"""learndjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from blog.views import *
from DjangoUeditor.views import get_ueditor_controller
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^(?P<article_id>[0-9]+)/', detail, name='detail'),
    url(r'^article/(?P<article_id>[0-9]+)',comment, name='comment'),
    url(r'^tag/(?P<tag_id>[0-9]+)/$', tag, name='tag'),
    url(r'^tag/(?P<tag_id>[0-9]+)/(?P<article_id>[0-9]+)/$', tag_detail, name='tagdetail'),
    url(r'^ueditor/controller/$', get_ueditor_controller),
    url(r'^search/$', search, name='search'),
    url(r'^test/$', test)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
