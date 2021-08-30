from django.urls import path
from .views import home_view, ProspectListView

app_name = 'prospectos'

urlpatterns = [
    path('', home_view, name='prospectos'),
    path('list/', ProspectListView.as_view(), name='list'),
]