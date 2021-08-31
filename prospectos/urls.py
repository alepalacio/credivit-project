from django.urls import path
from .views import home_view, ProspectListView, ProspectDetailView
#from .views import prospect_list_view, prospect_detail_view

app_name = 'prospectos'

urlpatterns = [
    path('', home_view, name='prospectos'),
    path('list/', ProspectListView.as_view(), name='list'),
    #path('lista/', prospect_list_view, name='lista'),
    path('detail/<pk>/', ProspectDetailView.as_view(), name='detail'),
    #path('details/<pk>/', prospect_detail_view, name='details')
]