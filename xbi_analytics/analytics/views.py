from django.shortcuts import render
import json as simplejson
from django.core import serializers
from analytics.models import GraphData, GridData, PieChartData

def analytics_index(request):
    graph_stats = GraphData.objects.all()
    graph_stats_serialized = serializers.serialize('json', graph_stats)
    
    grid_stats = GridData.objects.all()
    grid_stats_serialized = serializers.serialize('json', grid_stats)

    piechart_stats = PieChartData.objects.all()
    piechart_stats_serialized = serializers.serialize('json', piechart_stats)
    context = {
        'graph_stats': graph_stats_serialized, 
        'grid_stats': grid_stats_serialized,
        'piechart_stats': piechart_stats_serialized
    }
    return render(request, 'dashboard.html', context)
