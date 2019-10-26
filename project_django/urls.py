"""project_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from pages.views import home_view, huawei_view, xiaomi_view, sugestao_6ram
from celular.views import SearchResultsView
from loja.views import atualize_view
from pages import views


urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('sugestao_6ram/', sugestao_6ram, name='sugestao_6ram'),
    path('huawei/', huawei_view, name='huawei'),
    path('xiaomi/', xiaomi_view, name='xiaomi'),
    path('atualize/', atualize_view, name='atualize'),
    path('celular/<slug:slug>-<int:pk>', views.celular_details, name='detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]