from django.shortcuts import render
from django.views.generic import ListView
from .models import Prospect

# Create your views here.

def home_view(request):
    hello = 'hello world from this view'
    return render(request,'prospectos/home.html',{'hello':hello})

class ProspectListView(ListView):
    model = Prospect
    template_name = 'prospectos/main.html'
    # Default context_object_name = object_list in ListView
    context_object_name = 'prospectos'