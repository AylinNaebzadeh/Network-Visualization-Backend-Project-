from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('general_statistical_info/', general_statistical_info, name="get general statistical information"),
    path('top_5_nodes_based_on_several_measures/', top_5_nodes_based_on_several_measures, name="get top five nodes table"),
    path('degree_distribution/', degree_distribution, name='plot degree distribution'),
]