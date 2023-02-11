from django.shortcuts import render
from django.views.generic import View,TemplateView
import requests
import json
import os
from mySite.settings import LOOKUP_APP_ID, LOOKUP_APP_KEY

class Index(TemplateView):
    template_name='index.html'

class Lookup(View):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":

            if 'word' in request.GET:
                word = request.GET.get('word')
                endpoint = "entries"
                language_code = "en-us"
                url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word.lower()
                response = requests.get(url, headers = {"app_id": str(LOOKUP_APP_ID), "app_key": str(LOOKUP_APP_KEY)})
                r = json.loads(response.text)
                definition = r["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"]             

                context = {
                    'word' : word,
                    'definition' : definition,
                }
                return render(request, template_name="lookup.html", context=context)
        return render(request, template_name="lookup.html")
