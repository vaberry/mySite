from django.urls import path
from . import views

urlpatterns = [
   path('',views.Index.as_view(),name='index'),
   # path('lookup/', views.Lookup.as_view(), name='lookup'),
]