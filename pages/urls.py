from . import views
from django.urls import path



# URL leri tanımlarız.
urlpatterns = [
    path("",views.home,name="home"),
    path("anasayfa",views.home,name="home"),
    path("iletisim",views.iletisim,name="iletisim"),
    path("hakkimizda",views.hakkimizda,name="hakkimizda"),
]
