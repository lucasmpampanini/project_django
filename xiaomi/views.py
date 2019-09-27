from django.shortcuts import render
from xiaomi.models import Xiaomi
from django.views.generic import ListView
from django.db.models import Q

class SearchResultsView(ListView):
    model = Xiaomi
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q','')
        object_list = Xiaomi.objects.filter(
            Q(titlegb__icontains=query) | Q(pricegb__icontains=query) |
            Q(pricedx__icontains=query) | Q(pricebg__icontains=query) |
            Q(pricein__icontains=query)
        )

        return object_list