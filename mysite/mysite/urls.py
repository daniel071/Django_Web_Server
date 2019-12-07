"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from home.views import home_view
from army.views import army_view
from bibliography.views import bibliography_view
from republic.views import republic_view
from spartacus.views import spartacus_view
from technology.views import technology_view


urlpatterns = [
    path('djangoadmin/', admin.site.urls),
    path('home/', home_view),
    path('army/', army_view),
    path('bibliography/', bibliography_view),
    path('republic/', republic_view),
    path('spartacus/', spartacus_view),
    path('technology/', technology_view)
]
