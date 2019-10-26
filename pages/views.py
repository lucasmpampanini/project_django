from django.shortcuts import render
from django.http import Http404
from celular.models import Celular, Dolar
from loja.models import Loja
from django.views.generic import TemplateView, ListView
from django.db.models import Q


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

    if brand or ram or rom is not None:
        context = {'object_list': cell1,
                   'ram': ram,
                   'rom': rom,
                   'brand': brand,
                   }

        return render(request, "search_results.html", context)

    context = {'cell': cell1,
               'dolar': dolar,
               'cell_price_min': cell_price_min(request),
               # 'rom': rom_select(request),
               # 'ram': ram_select(request),
                #'pro_select': pro_select(request),
               # 'model': model_xiaomi(request),
               #'model': model_huawei(request),
               #'limpatitlebg': limpatitlebg(request),
               # 'some': some_select(request),
               # 'some': some2_select(request),
               #'bat': bat(request),
               #'tela': tela(request),
               #'teste': teste(request),
               #'new_title': new_title(request),
               }
    return render(request, "home.html", context)


def xiaomi_view(request, *args, **kwargs):
    cell1 = Celular.objects.all()
    cell1 = cell1.filter(title__contains="xiaomi")
    model = request.GET.get('model')
    if model is not None:
        cell1 = cell1.filter(title__contains=model)
        context = {'cell': cell1,
                   }
        return render(request, "xiaomi.html", context)

    context = {'cell': cell1,
               }

    return render(request, "xiaomi.html", context)


def huawei_view(request, *args, **kwargs):
    cell1 = Celular.objects.all()
    cell1 = cell1.filter(title__contains="huawei")
    model = request.GET.get('model')
    if model is not None:
        cell1 = cell1.filter(title__contains=model)
        context = {'cell': cell1,
                   }
        return render(request, "huawei.html", context)

    context = {'cell': cell1,
               }
    return render(request, "huawei.html", context)


def sugestao_6ram(request, *args, **kwargs):
    cell1 = Celular.objects.filter(titlegb__contains="6gb ram")

    context = {'cell': cell1,
               }
    return render(request, "sugestao_6ram.html", context)


def celular_details(request, pk, slug):
    try:
        celulares = Celular.objects.get(id=pk)
        a = celulares.ram
        if "6GB RAM" in a:
            cell = Celular.objects.filter(titlegb__contains="6gb ram")
            return render(request, 'details.html', {'cell': celulares, 'cell1': cell})
        elif "4GB RAM" in a:
            cell = Celular.objects.filter(titlegb__contains="4gb ram")
            return render(request, 'details.html', {'cell': celulares, 'cell1': cell})
        elif "8GB RAM" in a:
            cell = Celular.objects.filter(titlegb__contains="8gb ram")
            return render(request, 'details.html', {'cell': celulares, 'cell1': cell})
        else:
            return render(request, 'details.html', {'cell': celulares})
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
        # cellok.title = cellok.titlebg
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


def model_xiaomi(request):
    cell1 = Celular.objects.all()
    for cell in cell1:
        if "xiaomi" in cell.brand.lower():
            if not cell.model:
                cellok = Celular.objects.get(id=cell.id)
                cellok.model = cell.title.split()[1] + " " + cell.title.split()[2]
                if cell.title.split()[3].lower() == "lite":
                    cellok.model = cell.title.split()[1] + " " + cell.title.split()[2] + " " + cell.title.split()[3]
                if cell.title.split()[3].lower() == "pro":
                    cellok.model = cell.title.split()[1] + " " + cell.title.split()[2] + " " + cell.title.split()[3]
                if cell.title.split()[3].lower() == "plus":
                    cellok.model = cell.title.split()[1] + " " + cell.title.split()[2] + " " + cell.title.split()[3]
                if cell.title.split()[3].lower() == "se":
                    cellok.model = cell.title.split()[1] + " " + cell.title.split()[2] + " " + cell.title.split()[3]
                if cellok.title.split()[2].lower() == "note":
                    cellok.model = cell.title.split()[1] + " " + cell.title.split()[2] + " " + cell.title.split()[3]
                if cellok.title.split()[2].lower() == "mix":
                    cellok.model = cell.title.split()[1] + " " + cell.title.split()[2] + " " + cell.title.split()[3]
                if cellok.title.split()[2].lower() == "max":
                    cellok.model = cell.title.split()[1] + " " + cell.title.split()[2] + " " + cell.title.split()[3]
                if cellok.title.split()[4].lower() == "pro":
                    cellok.model = cell.title.split()[1] + " " + cell.title.split()[2] + " " + cell.title.split()[3] + " " + \
                                   cell.title.split()[4]
                cellok.save()


def limpatitlebg(request):
    cell1 = Celular.objects.all()
    for cell in cell1:
        if "banggood" in cell.store.lower():
            cellok = Celular.objects.get(id=cell.id)
            if cell.title.split()[1].lower() == "mi9" and cell.title.split()[2].lower() == "mi":
                title = cell.title.split()
                title.remove(title[1])
                cellok.title = title
                cellok.save()
            if cell.title.split()[1].lower() == "mi8" and cell.title.split()[2].lower() == "mi":
                title = cell.title.split()
                title.remove(title[1])
                cellok.title = title
                cellok.save()
    for cell in cell1:
        if "banggood" in cell.store.lower():
            cellok = Celular.objects.get(id=cell.id)
            if "['" in cell.title:
                cellok.title = cell.title.replace("[", "").replace("]", "").replace("'", "").replace(",", " ")
                cellok.save()

def model_huawei(request):
    cell1 = Celular.objects.all()
    for cell in cell1:
        if "huawei" in cell.brand.lower():
            cellok = Celular.objects.get(id=cell.id)
            if not cell.model:
                if cell.title.split()[3].lower() == "plus":
                    cellok.model = cell.title.split()[1] + " " + cell.title.split()[2] + " " + cell.title.split()[3]
                elif cell.title.split()[3].lower() == "lite":
                    cellok.model = cell.title.split()[1] + " " + cell.title.split()[2] + " " + cell.title.split()[3]
                elif cell.title.split()[3].lower() == "pro":
                    cellok.model = cell.title.split()[1] + " " + cell.title.split()[2] + " " + cell.title.split()[3]
                elif cell.title.split()[3].lower() == "play":
                    cellok.model = cell.title.split()[1] + " " + cell.title.split()[2] + " " + cell.title.split()[3]
                else:
                    cellok.model = cell.title.split()[1] + " " + cell.title.split()[2]
                cellok.save()

def pro_select(request):
    cell1 = Celular.objects.all()
    for cell in cell1:
        if not cell.pro:
            titleword = cell.title.split()
            for a in titleword:
                cellok = Celular.objects.get(id=cell.id)
                if "snapdragon" == a.lower():
                    cellok.pro = cell.title.split()[titleword.index(a)] + " " + cell.title.split()[titleword.index(a)+1] + " " + cell.title.split()[titleword.index(a)+2] + " " + cell.title.split()[titleword.index(a)+3]
                    cellok.save()
                if "kirin" == a.lower():
                    cellok.pro = cell.title.split()[titleword.index(a)] + " " + cell.title.split()[titleword.index(a)+1] + " " + cell.title.split()[titleword.index(a)+2] + " " + cell.title.split()[titleword.index(a)+3]
                    cellok.save()
                if "helio" == a.lower():
                    cellok.pro = "MediaTek " + cell.title.split()[titleword.index(a)] + " " + cell.title.split()[titleword.index(a)+1] + " " + cell.title.split()[titleword.index(a)+2] + " " + cell.title.split()[titleword.index(a)+3]
                    cellok.save()

def cam(request):
    cell1 = Celular.objects.all()
    for cell in cell1:
        if not cell.cam:
            titleword = cell.title.split()
            for a in titleword:
                cellok = Celular.objects.get(id=cell.id)
                if "MP" in a:
                    cellok.cam = cell.title.split()[titleword.index(a)]
                    cellok.save()
        if not cell.cam:
            titleword = cell.titlegb.split()
            for a in titleword:
                cellok = Celular.objects.get(id=cell.id)
                if "MP" in a:
                    cellok.cam = cell.titlegb.split()[titleword.index(a)]
                    cellok.save()

def bat(request):
    cell1 = Celular.objects.all()
    for cell in cell1:
        if not cell.bat:
            titleword = cell.title.split()
            for a in titleword:
                cellok = Celular.objects.get(id=cell.id)
                if "mAh" in a:
                    cellok.bat = cell.title.split()[titleword.index(a)]
                    cellok.save()
        if not cell.bat:
            titleword = cell.titlegb.split()
            for a in titleword:
                cellok = Celular.objects.get(id=cell.id)
                if "mAh" in a:
                    cellok.bat = cell.titlegb.split()[titleword.index(a)]
                    cellok.save()

def tela(request):
    cell1 = Celular.objects.all()
    for cell in cell1:
        if not cell.tela:
            titleword = cell.title.split()
            for a in titleword:
                cellok = Celular.objects.get(id=cell.id)
                if "inch" == a.lower():
                    cellok.tela = cell.title.split()[titleword.index(a)-1] + '"'
                    cellok.save()

def new_title(request):
    cell1 = Celular.objects.all()
    for cell in cell1:
        cellok = Celular.objects.get(id=cell.id)
        if cell.brand:
            newtitle = cell.brand.capitalize() + " "
        if cell.model:
            newtitle = newtitle + cell.model + " "
#        if cell.tela:
#           newtitle = newtitle + "Tela " + cell.tela + " "
#        if cell.pro:
#            newtitle = newtitle + cell.pro + " "
        if cell.ram:
            newtitle = newtitle + cell.ram + " "
        if cell.rom:
            newtitle = newtitle + cell.rom + " "
#        if cell.bat:
#            newtitle = newtitle + cell.bat + " "
#        if cell.cam:
#            newtitle = newtitle + "Camera " + cell.cam + " "

        cellok.title = newtitle
        cellok.save()