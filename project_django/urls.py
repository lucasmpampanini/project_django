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
from pages.views import home_view, huawei_view, xiaomi_view, sugestao_6ram, doogee_view, oneplus_view, \
bluboo_view, oukitel_view, lenovo_view, meizu_view, leagoo_view, asus_view, elephone_view, umidigi_view, \
cubot_view 
from celular.views import SearchResultsView
from chart.views import price_chart_view
from loja.views import atualize_view
from pages import views


urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('sugestao_6ram/', sugestao_6ram, name='sugestao_6ram'),
    path('xiaomi/', xiaomi_view, name='xiaomi'),
    path('huawei/', huawei_view, name='huawei'),
    path('doogee/', doogee_view, name='doogee'),
    path('oneplus/', oneplus_view, name='oneplus'),
    path('bluboo/', bluboo_view, name='bluboo'),
    path('oukitel/', oukitel_view, name='oukitel'),
    path('lenovo/', lenovo_view, name='lenovo'),
    path('meizu/', meizu_view, name='meizu'),
    path('leagoo/', leagoo_view, name='leagoo'),
    path('asus/', asus_view, name='asus'),
    path('elephone/', elephone_view, name='elephone'),
    path('umidigi/', umidigi_view, name='umidigi'),
    path('cubot/', cubot_view, name='cubot'),
    path('atualize/', atualize_view, name='atualize'),
    path('celular/<slug:slug>-<int:pk>', views.celular_details, name='detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('chart/', price_chart_view, name='chart'),
]