from django.shortcuts import render
from django.http import Http404
from xiaomi.models import Xiaomi, Dolar
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView, ListView

def home_view(request, *args, **kwargs):
    cell1 = Xiaomi.objects.all()
    dolar  =Dolar.objects.get(id=1)

    context = {'cell': cell1,
               'dolar': dolar,
               'teste': cell_price_min(request)
               }

    return render(request, "home.html", context)

def xiaomi_view(request, *args, **kwargs):
    cell1 = Xiaomi.objects.filter(titlegb__contains="xiaomi")

    context = {'cell': cell1,
               }

    return render(request, "xiaomi.html", context)

class SearchResultsView(ListView):
    model = Xiaomi
    template_name = 'search_results.html'

def huawei_view(request, *args, **kwargs):
    cell1 = Xiaomi.objects.filter(titlegb__contains="huawei")

    context = {'cell': cell1,
               }
    return render(request, "huawei.html", context)

def sugestao_6ram(request, *args, **kwargs):
    cell1 = Xiaomi.objects.filter(titlegb__contains="6gb ram")

    context = {'cell': cell1,
               }
    return render(request, "sugestao_6ram.html", context)

def xiaomi_196(request, pk):
  try:
    xiaomi = Xiaomi.objects.get(id=pk)
    a = xiaomi.titlegb
    if "6GB RAM" in a:
        cell = Xiaomi.objects.filter(titlegb__contains="6gb ram")
        return render(request, 'xiaomi/xiaomi_detail.html', {'xiaomi': xiaomi, 'cell': cell})
    elif "4GB RAM" in a:
        cell = Xiaomi.objects.filter(titlegb__contains="4gb ram")
        return render(request, 'xiaomi/xiaomi_detail.html', {'xiaomi': xiaomi, 'cell': cell})
    elif "8GB RAM" in a:
        cell = Xiaomi.objects.filter(titlegb__contains="8gb ram")
        return render(request, 'xiaomi/xiaomi_detail.html', {'xiaomi': xiaomi, 'cell': cell})
    else:
        return render(request, 'xiaomi/xiaomi_detail.html', {'xiaomi': xiaomi})
  except Xiaomi.DoesNotExist:
    raise Http404("Celular não existente")





def cell_price_min(request):
    cell1 = Xiaomi.objects.all()
    cotacao = Dolar.objects.get(id=1)
    for cell in cell1:
        list_price = [cell.pricegb, cell.pricebg, cell.pricedx, cell.pricein]
        list_priceok = [cell.pricegb, cell.pricebg, cell.pricedx, cell.pricein]
        list_url = [cell.urlgb, cell.urlbg, cell.urldx, cell.urlin]
        list_urlok = [cell.urlgb, cell.urlbg, cell.urldx, cell.urlin]
        list_name = [cell.namegb, cell.namebg, cell.namedx, cell.namein]
        cellok = Xiaomi.objects.get(id=cell.id)
        list_nameok = [cellok.namegb, cellok.namebg, cellok.namedx, cellok.namein]

        for b in list_price:
            if b == 0 or 0.00:
                list_priceok.remove(b)
            #else:
                #cal = b * cotacao.dolar_real
                #list_priceok[list_priceok.index(b)] = cal
        price_min = min(list_priceok)

        for b in list_url:
            if not b.replace('"', '$'):
                list_urlok.remove(b)
        url_min = list_priceok.index(min(list_priceok))

        for c in list_name:
            if "GearBest" in c:
                cellok.namegb = "/static/img/GearBest.png"
            if "Banggood" in c:
                cellok.namebg = "/static/img/banggoodlogo.png"
            if "Lightinthebox" in c:
                cellok.namein = "/static/img/Lightintheboxlogo.png"
            if "dealextreme" in c:
                cellok.namedx = "/static/img/dealextremelogo.png"
            if not c.replace('"', '$'):
                list_nameok.remove(c)
        name_min = list_priceok.index(min(list_priceok))
        cellok.pricegb_brl = cellok.pricegb * cotacao.dolar_real
        cellok.pricebg_brl = cellok.pricebg * cotacao.dolar_real
        cellok.pricedx_brl = cellok.pricedx * cotacao.dolar_real
        cellok.pricein_brl = cellok.pricein * cotacao.dolar_real
        cellok.best_price_brl = cellok.best_price * cotacao.dolar_real
        cellok.best_price = price_min
        cellok.best_url = list_urlok[url_min]
        cellok.best_name = list_nameok[name_min]
        cellok.save()

#{% widthratio cell1.pricegb 1 dolar %} multiplica um capo pelo outro.