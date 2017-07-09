"""hackthon URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from category.views import index

urlpatterns = [
    url(r'^$',index),
    url(r'^admin/', admin.site.urls),
    url(r'^play/',include('play.urls',namespace='play'),name='play'),
    url(r'^category/',include('category.urls',namespace='category'),name='category'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^car/',include('car.urls',namespace='car')),
]
