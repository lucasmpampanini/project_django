from django.contrib import admin
from xiaomi.models import Xiaomi, SearchXiaomi, Xiaomi_bg, SearchXiaomi_bg, Dolar

admin.site.register(Xiaomi, SearchXiaomi)
admin.site.register(Xiaomi_bg, SearchXiaomi_bg)
admin.site.register(Dolar)