from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.


def avg(request):
    queryset = Teachers.objects.only('salary')
    allSalary = [item.salary for item in queryset]
    avg = sum(allSalary) / len(allSalary)
    context = {}
    context['avg'] = avg
    return render(request, 'pz12.html', context=context)


def count(request):
    queryset = Teachers.objects.count()
    context = {}
    context['count'] = queryset
    return render(request, 'pz12.html', context=context)


def maxvalue(request):
    queryset = Teachers.objects.only('salary')
    allSalary = [item.salary for item in queryset]
    maxvalue = max(allSalary)
    context = {}
    context['maxvalue'] = maxvalue
    return render(request, 'pz12.html', context=context)


def minvalue(request):
    queryset = Teachers.objects.only('salary')
    allSalary = [item.salary for item in queryset]
    minvalue = min(allSalary)
    context = {}
    context['minvalue'] = minvalue
    return render(request, 'pz12.html', context=context)


def sumvalue(request):
    queryset = Teachers.objects.only('salary')
    allSalary = [item.salary for item in queryset]
    sumvalue = sum(allSalary)
    context = {}
    context['sumvalue'] = sumvalue
    return render(request, 'pz12.html', context=context)
