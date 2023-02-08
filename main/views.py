from django.shortcuts import render
from django.views.generic import View,TemplateView
# Create your views here.

class Index(TemplateView):
    template_name='index.html'

class Test(TemplateView):
    template_name='test.html'