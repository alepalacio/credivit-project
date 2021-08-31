from prospectos.models import Prospect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PreProspect
from .forms import PreProspectSearchForm

# Create your views here.

def home_view(request):
    form = PreProspectSearchForm(request.POST or None)
    
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        
        queryset = PreProspect.objects.all()
    context = {
        'form':form
    }
    return render(request, 'preprospectos/home.html', context)

class PreProspectListView(ListView):
    model = PreProspect
    template_name = 'preprospectos/main.html'
    context_object_name = 'preprospectos'
    
class PreProspectDetailView(DetailView):
    model = Prospect
    template_name = 'preprospectos/detail.html'