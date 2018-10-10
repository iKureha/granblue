# encoding: utf-8

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.html import format_html
from GranBlueModel.models import Granblue
from django.db.models import Q

Boss = Granblue

def testdb(boss_name):
    tip = '<div id="tip" style="position:absolute;visibility:hidden">Double click to copy to clipboard</div>'

    if boss_name == "all boss":
        result = Boss.objects.all().order_by('id').reverse()[0:20]
        response = []
        for var in result:
            temp = var.name + '</td><td>' + str(var.level) + '</td><td id="copy_to_clipboard" style="color":"#808080">' + tip + var.code
            temp = var.name + '</td><td>' + str(var.level) + '</td><td id="copy_to_clipboard">' + tip + var.code
            response.append(format_html(temp))

    else:
        if boss_name == "Colossus":
            result = Boss.objects.filter(Q(name__contains="Colossus") | Q(name__contains="コロッサス")).order_by('id').reverse()[0:8]
        elif boss_name == "Tiamat":
            result = Boss.objects.filter(Q(name__contains="Tiamat") | Q(name__contains="ティアマト")).order_by('id').reverse()[0:8]
        elif boss_name == "Leviathan":
            result = Boss.objects.filter(Q(name__contains="Leviathan") | Q(name__contains="リヴァイアサン")).order_by('id').reverse()[0:8]
        elif boss_name == "Yggdrasil":
            result = Boss.objects.filter(Q(name__contains="Yggdrasil") | Q(name__contains="ユグドラシル")).order_by('id').reverse()[0:8]
        elif boss_name == "Celeste":
            result = Boss.objects.filter(Q(name__contains="Celeste") | Q(name__contains="セレスト")).order_by('id').reverse()[0:8]
        elif boss_name == "Luminiera":
            result = Boss.objects.filter(Q(name__contains="Luminiera") | Q(name__contains="シュヴァリエ")).order_by('id').reverse()[0:8]
        else:
            pass

        response = []
        for var in result:
            temp = str(var.level) + '</td><td id="copy_to_clipboard" style="color":"#808080">' + tip + var.code
            response.append(format_html(temp))

    return response


def ajax_db(boss_name):
        if boss_name == "Colossus":	
            result = Boss.objects.filter(name="Colossus").order_by('id').reverse()[0:8]
        elif boss_name == "Tiamat":
            result = Boss.objects.filter(name="Tiamat").order_by('id').reverse()[0:8]
        elif boss_name == "Leviathan":
            result = Boss.objects.filter(name="Leviathan").order_by('id').reverse()[0:8]
        elif boss_name == "Yggdrasil":
            result = Boss.objects.filter(name="Yggdrasil").order_by('id').reverse()[0:8]
        elif boss_name == "Celeste":
            result = Boss.objects.filter(name="Celeste").order_by('id').reverse()[0:8]
        elif boss_name == "Luminiera":
            result = Boss.objects.filter(name="Luminiera").order_by('id').reverse()[0:8]
        else:
            result = Boss.objects.filter(name="Celeste").order_by('id').reverse()[0:8]

        response = []
        for var in result:
            temp = str(var.level) + '</td><td id="copy_to_clipboard">' + tip + var.code
            response.append(format_html(temp))
        return response


def ajax_db(boss_name):

    if boss_name == "Colossus":
        result = Boss.objects.filter(Q(name__contains="Colossus") | Q(name__contains="コロッサス")).order_by('id').reverse()[0:8]
    elif boss_name == "Tiamat":
        result = Boss.objects.filter(Q(name__contains="Tiamat") | Q(name__contains="ティアマト")).order_by('id').reverse()[0:8]
    elif boss_name == "Leviathan":
        result = Boss.objects.filter(Q(name__contains="Leviathan") | Q(name__contains="リヴァイアサン")).order_by('id').reverse()[0:8]
    elif boss_name == "Yggdrasil":
        result = Boss.objects.filter(Q(name__contains="Yggdrasil") | Q(name__contains="ユグドラシル")).order_by('id').reverse()[0:8]
    elif boss_name == "Celeste":
        result = Boss.objects.filter(Q(name__contains="Celeste") | Q(name__contains="セレスト")).order_by('id').reverse()[0:8]
    elif boss_name == "Luminiera":
        result = Boss.objects.filter(Q(name__contains="Luminiera") | Q(name__contains="シュヴァリエ")).order_by('id').reverse()[0:8]
        result = Boss.objects.filter(name="Colossus").order_by('id').reverse()[0:8]
    elif boss_name == "Tiamat":
        result = Boss.objects.filter(name="Tiamat").order_by('id').reverse()[0:8]
    elif boss_name == "Leviathan":
        result = Boss.objects.filter(name="Leviathan").order_by('id').reverse()[0:8]
    elif boss_name == "Yggdrasil":
        result = Boss.objects.filter(name="Yggdrasil").order_by('id').reverse()[0:8]
    elif boss_name == "Celeste":
        result = Boss.objects.filter(name="Celeste").order_by('id').reverse()[0:8]
    elif boss_name == "Luminiera":
        result = Boss.objects.filter(name="Luminiera").order_by('id').reverse()[0:8]
    else:
        result = Boss.objects.all().order_by('id').reverse()[0:20]

    response = []
    for var in result:
        temp = var.name + ',' + str(var.level) + ',' + var.code
        response.append(temp)

    return response


def index(request):
    context = {}
    context['welcome'] = 'Welcome to this site!!! '
    context['all_boss'] = testdb("all boss")
    context['tiamat'] = testdb("Tiamat")
    context['leviathan'] = testdb("Leviathan")
    context['colossus'] = testdb("Colossus")
    context['yggdrasil'] = testdb("Yggdrasil")
    context['luminiera'] = testdb("Luminiera")
    context['celeste'] = testdb("Celeste")
    return render(request, 'index.html', context)


def ajax_all_boss(request):
    res = ajax_db("all boss")
    return JsonResponse(res, safe=False)


def ajax_tiamat(request):
    res = ajax_db("Tiamat")
    return JsonResponse(res, safe=False)


def ajax_colossus(request):
    res = ajax_db("Colossus")
    return JsonResponse(res, safe=False)


def ajax_leviathan(request):
    res = ajax_db("Leviathan")
    return JsonResponse(res, safe=False)


def ajax_yggdrasil(request):
    res = ajax_db("Yggdrasil")
    return JsonResponse(res, safe=False)


def ajax_celeste(request):
    res = ajax_db("Celeste")
    return JsonResponse(res, safe=False)


def ajax_luminiera(request):
    res = ajax_db("Luminiera")
    return JsonResponse(res, safe=False)

def index_test(request):
    context = {}
    context['welcome'] = 'This is a test site! '
    context['all_boss'] = testdb("all boss")
    context['tiamat'] = testdb("Tiamat")
    context['leviathan'] = testdb("Leviathan")
    context['colossus'] = testdb("Colossus")
    context['yggdrasil'] = testdb("Yggdrasil")
    context['luminiera'] = testdb("Luminiera")
    context['celeste'] = testdb("Celeste")
    return render(request, 'index_test.html', context)

