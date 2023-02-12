from django.urls import path
from . import views

urlpatterns = [
   path('',views.Home.as_view(),name='home'),
   path('lookup/', views.Lookup.as_view(), name='lookup'),
   path('scraper/', views.Scraper.as_view(), name='scraper'),
]