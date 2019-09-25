from django.shortcuts import render
from xiaomi.models import Xiaomi, Dolar
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
    cell1 = Xiaomi.objects.all()

    context = {'cell': cell1,
               }

    return render(request, "xiaomi.html", context)

class SearchResultsView(ListView):
    model = Xiaomi
    template_name = 'search_results.html'

def celulares_view(request, *args, **kwargs):
    cell1 = Xiaomi.objects.all()

    context = {'cell': cell1,
               }
    return render(request, "celulares.html", context)

def cell_price_min(request):
    cell1 = Xiaomi.objects.all()
    cotacao = Dolar.objects.get(id=1)
    for cell in cell1:
        list_price = [cell.pricegb, cell.pricebg, cell.pricedx, cell.pricein]
        list_priceok = [cell.pricegb, cell.pricebg, cell.pricedx, cell.pricein]
        list_url = [cell.urlgb, cell.urlbg, cell.urldx, cell.urlin]
        list_urlok = [cell.urlgb, cell.urlbg, cell.urldx, cell.urlin]
        list_name = [cell.namegb, cell.namebg, cell.namedx, cell.namein]
        list_nameok = [cell.namegb, cell.namebg, cell.namedx, cell.namein]

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
            if not c.replace('"', '$'):
                list_nameok.remove(c)
        name_min = list_priceok.index(min(list_priceok))
        cellok = Xiaomi.objects.get(id=cell.id)
        cellok.best_price = price_min
        cellok.best_url = list_urlok[url_min]
        cellok.best_name = list_nameok[name_min]
        cellok.save()

#{% widthratio cell1.pricegb 1 dolar %} multiplica um capo pelo outro.