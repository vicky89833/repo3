from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Hello_view(request):
    return HttpResponse('<h1>Hi ,U  r welcome ! on Vicky,s website</h1>')
