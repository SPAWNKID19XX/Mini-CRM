from django.shortcuts import render, HttpResponse

def health_ok(request):
    return HttpResponse('OK')
