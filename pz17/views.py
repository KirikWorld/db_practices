from django.http import HttpResponse
from django.shortcuts import render
from pz12.models import *
from django.db.models import Max

def triggers(request):
    # пример создания нового предмета
    # все что делается здесь, является аналогичным созданию курса из примера к практике
    queryset = Subjects.objects.all().aggregate(Max('tcode'))
    subjectname = Subjects.objects.filter(tcode=f'{queryset["tcode__max"]}')
    subjectsname = ", ".join([str(item) for item in subjectname])
    s = Subjects(title='База данных', tcode=queryset["tcode__max"]+1)
    print(s.save())
    return HttpResponse(f'Максимальное код дисциплины: {queryset["tcode__max"]}<br>Список названий дисциплин с таким значением: {subjectsname}')
