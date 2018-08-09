# encoding: utf-8

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.html import format_html
from GranBlueModel.models import Granblue

Boss = Granblue

def testdb(boss_name):
    tip = '<div id="tip" style="position:absolute;visibility:hidden">Double click to copy to clipboard</div>'

    if boss_name == "all boss":
        result = Boss.objects.all().order_by('id').reverse()[0:20]
        response = []
        for var in result:
            temp = var.name + '</td><td>' + str(var.level) + '</td><td id="copy_to_clipboard">' + tip + var.code
            response.append(format_html(temp))

    else:
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



# database
# conn = sqlite3.connect('/Users/wang 1/GranBlue/boss.db')
# conn = sqlite3.connect('boss.db')
# print("Linked to SQLite database !")
# cursor = conn.cursor()
# cursor.execute('create table tiamat (code varchar(8))')
# print(cursor.rowcount)
# sql = 'select id, name, lvl, code from boss order by id desc limit 20'
# cursor.execute(sql)
# to_return = []
# for i in cursor:
#     # a = i.name + str(i.lvl) + i.code
#     row = i[1] + '</td><td>' + str(i[2]) + '</td><td id="copy_to_clipboard">' + i[3]
#     to_return.append(format_html(row))






