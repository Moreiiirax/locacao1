from django.urls import path
from . import views

app_name = 'locacoes'
urlpatterns = [
    path('', views.LocacaoListView.as_view(), name='lista'),
    path('novo/', views.LocacaoCreateView.as_view(), name='novo'),
]