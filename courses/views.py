from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
data = {
    "programlama":"Programlama Kategorisine ait kurslar",
    "web-gelistirme":"Web-Gelistirme Kategorisine ait kurslar",
    "mobil":"Mobil Kategorisine ait kurslar"
}

# Create your views here.
def kurslar(request):
    return HttpResponse("KURS Listesi")

def details(request,kurs_adi):
    return HttpResponse(f"{kurs_adi} DETAYLARI")

def programlama(request):
    return HttpResponse("PROGRAMLAMA KURSU")

def mobiluygulamalar(request):
    return HttpResponse("MOBİL UYGULAMALAR")

#category_name ile urls içindeki category_name aynı adlandırılmak zorunda
def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponse("YANLIŞ KATEGORİ SEÇİMİ")

def getCoursesByCategoryId(request, category_id):
    # Sözlüğün keys lerini alır . --> programlama,web-gelistirme,mobil
    # Bunu listeye koyar ve listenin içinde verilen category_id - 1 e göre 
    # listeler. liste 0 dan başlar url den giren kişi 1 den yazmaya başlar. -1 gelmesinin sebebi de budur.
    category_list = list(data.keys())
    if category_id > len(category_list):
        return HttpResponseNotFound("YANLIŞ KATEGORİ SEÇİMİ")
    
    category_name = category_list[category_id - 1]
    # Otomatik olarak url almasını sağladık. Bu sayede başka bir zaman
    # urls i değişirse burası da onunla birlikte otomatik değişicek.
    redirect_url = reverse("courses_by_category",args=[category_name])
    return redirect(redirect_url)