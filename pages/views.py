from django.shortcuts import render
from django.http import Http404
from celular.models import Celular, Dolar
from loja.models import Loja
from django.views.generic import TemplateView, ListView
from django.db.models import Q

def is_valid_queryparam(param):
    return param != '' and param is not None

def home_view(request, *args, **kwargs):
    cell1 = Celular.objects.all()
    dolar = Dolar.objects.get(id=1)
    brand = request.GET.get('brand')
    ram = request.GET.get('ram')
    rom = request.GET.get('rom')
    if brand is not None:
        cell1 = cell1.filter(title__contains=brand)

    if ram is not None:
        cell1 = cell1.filter(title__contains=ram)

    if rom is not None:
        cell1 = cell1.filter(title__contains=rom)


    context = {'cell': cell1,
                   'dolar': dolar,
                   'teste': cell_price_min(request),
                    'ram': ram,
                    'rom': rom,
                    'brand': brand,
                   # 'rom': rom_select(request),
                   # 'ram': ram_select(request),
                   # 'atualizar': select(request),
                   # 'some': some_select(request),
                   # 'some': some2_select(request),
                   }



    return render(request, "home.html", context)





def xiaomi_view(request, *args, **kwargs):
    cell1 = Celular.objects.filter(titlegb__contains="xiaomi")

    context = {'cell': cell1,
               }

    return render(request, "xiaomi.html", context)

def huawei_view(request, *args, **kwargs):
    cell1 = Celular.objects.filter(titlegb__contains="huawei")

    context = {'cell': cell1,
               }
    return render(request, "huawei.html", context)


def sugestao_6ram(request, *args, **kwargs):
    cell1 = Celular.objects.filter(titlegb__contains="6gb ram")

    context = {'cell': cell1,
               }
    return render(request, "sugestao_6ram.html", context)


def xiaomi_196(request, pk):
    try:
        xiaomi = Celular.objects.get(id=pk)
        a = xiaomi.ram
        if "6GB RAM" in a:
            cell = Celular.objects.filter(titlegb__contains="6gb ram")
            return render(request, 'xiaomi/xiaomi_detail.html', {'xiaomi': xiaomi, 'cell': cell})
        elif "4GB RAM" in a:
            cell = Celular.objects.filter(titlegb__contains="4gb ram")
            return render(request, 'xiaomi/xiaomi_detail.html', {'xiaomi': xiaomi, 'cell': cell})
        elif "8GB RAM" in a:
            cell = Celular.objects.filter(titlegb__contains="8gb ram")
            return render(request, 'xiaomi/xiaomi_detail.html', {'xiaomi': xiaomi, 'cell': cell})
        else:
            return render(request, 'xiaomi/xiaomi_detail.html', {'xiaomi': xiaomi})
    except Celular.DoesNotExist:
        raise Http404("Celular não existente")


def cell_price_min(request):
    cell1 = Celular.objects.all()
    cotacao = Dolar.objects.get(id=1)
    for cell in cell1:
        list_price = [cell.pricegb, cell.pricebg, cell.pricedx, cell.pricein]
        list_priceok = [cell.pricegb, cell.pricebg, cell.pricedx, cell.pricein]
        list_url = [cell.urlgb, cell.urlbg, cell.urldx, cell.urlin]
        list_urlok = [cell.urlgb, cell.urlbg, cell.urldx, cell.urlin]
        list_name = [cell.namegb, cell.namebg, cell.namedx, cell.namein]
        cellok = Celular.objects.get(id=cell.id)
        list_nameok = [cellok.namegb, cellok.namebg, cellok.namedx, cellok.namein]

        for b in list_price:
            if b == 0 or 0.00:
                list_priceok.remove(b)
            # else:
            # cal = b * cotacao.dolar_real
            # list_priceok[list_priceok.index(b)] = cal
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

        if not list_url[0].replace('"', '$'):
            cellok.url_img = cellok.url_img_bg
            cellok.save()
        else:
            cellok.url_img = cellok.url_img_gb
            cellok.save()
        cellok.title = cellok.titlebg
        cellok.pricegb_brl = cellok.pricegb * cotacao.dolar_real
        cellok.pricebg_brl = cellok.pricebg * cotacao.dolar_real
        cellok.pricedx_brl = cellok.pricedx * cotacao.dolar_real
        cellok.pricein_brl = cellok.pricein * cotacao.dolar_real
        cellok.best_price_brl = cellok.best_price * cotacao.dolar_real
        cellok.best_price = price_min
        cellok.best_url = list_urlok[url_min]
        cellok.best_name = list_nameok[name_min]
        cellok.save()


# {% widthratio cell1.pricegb 1 dolar %} multiplica um capo pelo outro.

def select(request):
    cell1 = Celular.objects.all()
    for cell in cell1:
        if not cell.ram:
            cellok = Celular.objects.get(id=cell.id)
            cellok.title = "Atualizar"
            cellok.save()

        if not cell.rom:
            cellok = Celular.objects.get(id=cell.id)
            cellok.title = "Atualizar"
            cellok.save()


def same_select(request):
    cell1 = Celular.objects.all()
    for cell in cell1:
        if "6GB" in cell.ram:
            cellok = Celular.objects.get(id=cell.id)
            cellok.title = ""
            cellok.save()


def rom_select(request):
    cell1 = Celular.objects.all()
    for cell in cell1:
        if " 16gb " in cell.title.lower():
            cellok = Celular.objects.get(id=cell.id)
            cellok.rom = "16GB ROM"
            cellok.save()

    for cell in cell1:
        if " 32gb " in cell.title.lower():
            cellok = Celular.objects.get(id=cell.id)
            cellok.rom = "32GB ROM"
            cellok.save()

    for cell in cell1:
        if " 64gb " in cell.title.lower():
            cellok = Celular.objects.get(id=cell.id)
            cellok.rom = "64GB ROM"
            cellok.save()

    for cell in cell1:
        if " 128gb " in cell.title.lower():
            cellok = Celular.objects.get(id=cell.id)
            cellok.rom = "128GB ROM"
            cellok.save()

    for cell in cell1:
        if " 256gb " in cell.title.lower():
            cellok = Celular.objects.get(id=cell.id)
            cellok.rom = "256GB ROM"
            cellok.save()

    for cell in cell1:
        if " 512gb " in cell.title.lower():
            cellok = Celular.objects.get(id=cell.id)
            cellok.rom = "512GB ROM"
            cellok.save()


def ram_select(request):
    cell1 = Celular.objects.all()
    for cell in cell1:
        if " 1gb " in cell.title.lower():
            cellok = Celular.objects.get(id=cell.id)
            cellok.ram = "1GB RAM"
            cellok.save()

    for cell in cell1:
        if " 2gb " in cell.title.lower():
            cellok = Celular.objects.get(id=cell.id)
            cellok.ram = "2GB RAM"
            cellok.save()

    for cell in cell1:
        if " 3gb " in cell.title.lower():
            cellok = Celular.objects.get(id=cell.id)
            cellok.ram = "3GB RAM"
            cellok.save()

    for cell in cell1:
        if " 4gb " in cell.title.lower():
            cellok = Celular.objects.get(id=cell.id)
            cellok.ram = "4GB RAM"
            cellok.save()

    for cell in cell1:
        if " 6gb " in cell.title.lower():
            cellok = Celular.objects.get(id=cell.id)
            cellok.ram = "6GB RAM"
            cellok.save()

    for cell in cell1:
        if " 8gb " in cell.title.lower():
            cellok = Celular.objects.get(id=cell.id)
            cellok.ram = "8GB RAM"
            cellok.save()

    for cell in cell1:
        if " 10gb " in cell.title.lower():
            cellok = Celular.objects.get(id=cell.id)
            cellok.ram = "10GB RAM"
            cellok.save()

    for cell in cell1:
        if " 12gb " in cell.title.lower():
            cellok = Celular.objects.get(id=cell.id)
            cellok.ram = "12GB RAM"
            cellok.save()


def some2_select(request):
    cell1 = Celular.objects.filter(titlegb__contains="HUAWEI nova 5 Pro ")
    cell2 = Celular.objects.filter(titlebg__contains="HUAWEI nova 5 Pro ")
    for cell in cell1:
        for cel in cell2:
            if cell.ram == cel.ram and cell.rom == cel.rom:
                cellok = Celular.objects.get(id=cell.id)
                celdel = Celular.objects.get(id=cel.id)
                cellok.titlebg = celdel.titlebg
                cellok.urlbg = celdel.urlbg
                cellok.pricebg = celdel.pricebg
                cellok.namebg = celdel.namebg
                cellok.save()
                celdel.delete()
