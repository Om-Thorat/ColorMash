from django.urls import path
import re
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vote/', views.vote, name='vote'),
    path('leads',views.results, name='leads'),
]