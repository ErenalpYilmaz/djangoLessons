from . import views
from django.urls import path



# URL leri tanımlarız.
urlpatterns = [
    path("",views.home,name="home")
]
