from django.shortcuts import render
from xiaomi.models import Xiaomi
from django.views.generic import ListView
from django.db.models import Q

class SearchResultsView(ListView):
    model = Xiaomi
    template_name = 'search_results.html'

    def get_queryset(self):
        cell1 = Xiaomi.objects.all()
        best_price = {'cell': cell1,
                      'cell0': cell_price_min(cell1[0]),
                      'cell01': cell_price_min(cell1[1]),
                      'cell2': cell_price_min(cell1[2]),
                      'cell3': cell_price_min(cell1[3]),
                      'cell4': cell_price_min(cell1[4]),
                      'cell5': cell_price_min(cell1[5]),
                      'cell6': cell_price_min(cell1[6]),
                      'cell7': cell_price_min(cell1[7]),
                      'cell8': cell_price_min(cell1[8]),
                      'cell9': cell_price_min(cell1[9]),
                      'cell10': cell_price_min(cell1[10]),
                      'cell11': cell_price_min(cell1[11]),
                      'cell12': cell_price_min(cell1[12]),
                      'cell13': cell_price_min(cell1[13]),
                      'cell14': cell_price_min(cell1[14]),
                      'cell15': cell_price_min(cell1[15]),
                      'cell16': cell_price_min(cell1[16]),
                      'cell17': cell_price_min(cell1[17]),
                      'cell18': cell_price_min(cell1[18]),
                      'cell19': cell_price_min(cell1[19]),
                      'cell20': cell_price_min(cell1[20]),
                      'cell21': cell_price_min(cell1[21]),
                      'cell22': cell_price_min(cell1[22]),
                      'cell23': cell_price_min(cell1[23]),
                      'cell24': cell_price_min(cell1[24]),
                      'cell25': cell_price_min(cell1[25]),
                      'cell26': cell_price_min(cell1[26]),
                      }

        query = self.request.GET.get('q','')
        object_list = Xiaomi.objects.filter(
            Q(titlegb__icontains=query) | Q(pricegb__icontains=query) |
            Q(pricedx__icontains=query) | Q(pricebg__icontains=query) |
            Q(pricein__icontains=query)
        ), best_price

        return object_list

def cell_price_min(cell):
    list_price = [cell.pricegb, cell.pricebg, cell.pricedx, cell.pricein]
    list_priceok = [cell.pricegb, cell.pricebg, cell.pricedx, cell.pricein]
    list_url = [cell.urlgb, cell.urlbg, cell.urldx, cell.urlin]
    list_urlok = [cell.urlgb, cell.urlbg, cell.urldx, cell.urlin]
    list_name = [cell.namegb, cell.namebg, cell.namedx, cell.namein]
    list_nameok = [cell.namegb, cell.namebg, cell.namedx, cell.namein]

    for b in list_price:
        if b == 0 or 0.00:
            list_priceok.remove(b)
    price_min = min(list_priceok)

    for b in list_url:
        if not b.replace('"', '$'):
            list_urlok.remove(b)
    url_min = list_priceok.index(min(list_priceok))

    for c in list_name:
        if not c.replace('"', '$'):
            list_nameok.remove(c)
    name_min = list_priceok.index(min(list_priceok))

    return [price_min, list_urlok[url_min], list_nameok[name_min]]