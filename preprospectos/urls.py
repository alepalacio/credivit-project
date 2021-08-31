from django.urls import path
from .views import home_view, PreProspectListView, PreProspectDetailView

app_name = 'preprospectos'

urlpatterns = [
    path('', home_view, name='home'),
    path('list/', PreProspectListView.as_view(), name='list'),
    path('detail/<pk>/', PreProspectDetailView.as_view(), name='detail'),
]