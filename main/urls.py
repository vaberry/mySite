from django.urls import path
from . import views

urlpatterns = [
   path('',views.Index.as_view(),name='index'),
   path('test/', views.Test.as_view(), name='test'),
]