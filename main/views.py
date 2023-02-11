from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View,TemplateView
from pydictionary import Dictionary

class Index(TemplateView):
    template_name='index.html'

# class Lookup(View):
#     def get(self, request, *args, **kwargs):
#         if request.method == "GET":
#             if 'word' in request.GET:
#                 word = request.GET.get("word")
#                 response = Dictionary(word).meanings()
#                 if len(response) == 0:
#                     response.append('Could not find that word...')

#                 context = {
#                     'word' : word,
#                     'definition' : response
#                 }
#                 return render(request, template_name="lookup.html", context=context)
#         return render(request, template_name="lookup.html")
