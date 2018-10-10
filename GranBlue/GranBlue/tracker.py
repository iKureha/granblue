# -*- encoding: utf-8 -*-

def tracker():
    

def ajax_tracker(request):
    res = tracker("Luminiera")
    return JsonResponse(res, safe=False)
