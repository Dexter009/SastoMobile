from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView, FormView

from sastobazaar.models import DarazItem, NepBayItem
from .forms import SearchForm


class HomeView(FormView):
    template_name = "home.html"
    form_class = SearchForm

def search_result(request):
    if 'name' in request.GET and request.GET['name']:
        search_term=request.GET['name']
        #qset = Q()
        #for term in search_term.split():
        #    qset |= Q(title__icontains=term)
        results=DarazItem.objects.filter(title__icontains=search_term)
        results1 = NepBayItem.objects.filter(title__icontains=search_term)

        context={'results':results,'results1':results1, 'search_term':search_term}
    else:
        context={}
    return render(request,"search_result.html",context)

