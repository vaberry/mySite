from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View,TemplateView
import requests
import json
import os
import configparser

class Index(TemplateView):
    template_name='index.html'

class Lookup(View):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            if 'word' in request.GET:
                word = request.GET.get('word')
                config = configparser.ConfigParser()
                config.read('.env')
                APP_KEY = config.get('APP', 'APP_KEY')
                APP_ID = config.get('APP', 'APP_ID')
                endpoint = "entries"
                language_code = "en-us"
                url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word.lower()
                response = requests.get(url, headers = {"app_id": str(APP_ID), "app_key": str(APP_KEY)})
                r = json.loads(response.text)
                definition = r["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"]             

                context = {
                    'word' : word,
                    'definition' : definition,
                }
                return render(request, template_name="lookup.html", context=context)
        return render(request, template_name="lookup.html")
