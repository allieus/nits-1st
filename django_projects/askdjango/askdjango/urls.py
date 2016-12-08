"""askdjango URL Configuration

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
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from blog import views as blog_views
from dojo import views as dojo_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', blog_views.post_list, name='post_list'),
    url(r'^(?P<pk>\d+)/$', blog_views.post_detail, name='post_detail'),
    url(r'^sum/(?P<numbers>[\d\/]+)/$', dojo_views.mysum, name='mysum'),
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', dojo_views.hello, name='hello'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

