from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Prospect
from .forms import ProspectSearchForm

import pandas as pd

# Create your views here.

def home_view(request):
    prospectos_df = None
    positions_df = None
    form = ProspectSearchForm(request.POST or None)
    
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        print(date_from, date_to, chart_type)
        
        #queryset = Prospect.objects.all()
        queryset = Prospect.objects.filter(created_at__date__lte=date_to, created_at__date__gte=date_from)
        # print('Simple queryset', queryset)
        # print('queryset.values', queryset.values())
        # print('queryset.values_list', queryset.values_list())
        # print('##############')
        if len(queryset) > 0:
            prospectos_df = pd.DataFrame(queryset.values())
            prospectos_df = prospectos_df.to_html()
            #print(prospectos_df)
        else:
            print('No data')
            
    context = {
        'form': form,
        'prospectos_df': prospectos_df
    }
    return render(request,'prospectos/home.html', context)

class ProspectListView(ListView):
    model = Prospect
    template_name = 'prospectos/main.html'
    # Default context_object_name = object_list in ListView
    context_object_name = 'prospectos'
    
class ProspectDetailView(DetailView):
    model = Prospect
    template_name = 'prospectos/detail.html'
    
    
# def prospect_list_view(request):
#     """
#     Function based view, same as ProspectListView. Key context has to be the same than the context_object_name. By default is: object_list.
#     """
#     queryset = Prospect.objects.all()
#     return render(request, 'prospectos/main.html', {'prospectos': queryset})

# def prospect_detail_view(request, pk):
#     """
#     Function based view, same as ProspectDetailView. Key context has to be the same than the template iterator on content. By default is: object.
#     """
#     obj = Prospect.objects.get(pk=pk)
#     # or
#     # obj = get_object_or_404(Prospect, pk=pk)
#     return render(request, 'prospectos/detail.html', {'object': obj})