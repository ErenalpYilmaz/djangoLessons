from . import views
from django.urls import path



# URL leri tanımlarız. --> Yönlenirmeler
urlpatterns = [
    path("",views.kurslar,name="kurslar"),
    path("list",views.kurslar,name="kurslar"),
    path("<kurs_adi>",views.details,name="details"),
    # Dinamik url ler her zaman alta yazdırır.
    path("kategori/<int:category_id>",views.getCoursesByCategoryId,name="getCoursesByCategory"),
    # 127.0.0.1:8000/kurs/x   x--> yerine ne yazarsan bu kısımda çalışıyor. Altta olması önemli    
    path("kategori/<str:category_name>",views.getCoursesByCategory,name ="courses_by_category"),

]

#courseapp
#courses
#pages