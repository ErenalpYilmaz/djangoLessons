from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("ANASAYFA")

def iletisim(request):
    return HttpResponse("İLETİŞİM SAYFASI")

def hakkimizda(request):
    return HttpResponse("HAKKIMIZDA SAYFASI")