from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View,TemplateView
import requests
import json
from config import APP_ID, APP_KEY
# from pydictionary import Dictionary

class Index(TemplateView):
    template_name='index.html'

class Lookup(View):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            if 'word' in request.GET:
                word = request.GET.get('word')
                app_id = APP_ID
                app_key = APP_KEY
                endpoint = "entries"
                language_code = "en-us"
                word_id = "example"
                url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word.lower()
                response = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})
                print(type(response.text))
                print(type(json.loads(response.text)))
                r = json.loads(response.text)
                print(r["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"])                

                context = {
                    'word' : word,
                    'definition' : r
                }
                return render(request, template_name="lookup.html", context=context)
        return render(request, template_name="lookup.html")
