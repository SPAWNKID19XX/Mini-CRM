from django.shortcuts import render, HttpResponse

def health_ok(request):
    print('OK')
    return HttpResponse('OK')
