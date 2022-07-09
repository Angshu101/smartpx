from django.urls import path
from . import views
urlpatterns = [
    path('',views.phonex,name="phonex"),
    path('search',views.search,name="search"),
]