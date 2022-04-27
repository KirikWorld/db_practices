from django.http import HttpResponse
from django.shortcuts import render
from pz12.models import *

# Create your views here.
def tablesconnection(request):
    queryset = Teachers.objects.select_related()
    queryset = [f"{item.subject}: {item.subject.tcode}" for item in queryset]
    context = {}
    context['connections'] = queryset
    return render(request, 'pz13.html', context=context)

def inneragregate(request):
    querysetf = Teachers.objects.filter(subject__title='Физика')
    queryseth = Teachers.objects.filter(subject__title='Химия')
    querysetf, queryseth = [item.salary for item in querysetf], [item.salary for item in queryseth]
    querysetf, queryseth = sum(querysetf), sum(queryseth)
    context = {}
    context['fizika'], context['himia'] = querysetf, queryseth
    return render(request, 'pz13.html', context=context)