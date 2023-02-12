from django.shortcuts import render
from django.views.generic import View,TemplateView
import requests
import json
import os
from mySite.settings import DEVELOPMENT_MODE
from dotenv import load_dotenv

load_dotenv()

class Index(TemplateView):
    template_name='index.html'

class Lookup(View):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            print('DEVELOPMENT MODE IS', DEVELOPMENT_MODE)
            if 'word' in request.GET:
                word = request.GET.get('word')
                LOOKUP_APP_ID = os.getenv("LOOKUP_APP_ID")
                LOOKUP_APP_KEY = os.getenv("LOOKUP_APP_KEY")
                endpoint = "entries"
                language_code = "en-us"
                url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word.lower()
                if not DEVELOPMENT_MODE:
                    response = requests.get(url, headers = {"app_id": str(os.getenv('APP_ID')), "app_key": str(os.getenv('APP_KEY'))})
                else:
                    response = requests.get(url, headers = {"app_id": str(LOOKUP_APP_ID), "app_key": str(LOOKUP_APP_KEY)})

                r = json.loads(response.text)
                try:
                    definition = r["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"]
                except:
                    definition = ["No definitions found..."]
                try:
                    synonyms = r["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["synonyms"]
                    synonyms = [i['text'] for i in synonyms]
                except:
                    synonyms = ["No synonyms found..."]
                try:
                    examples = r["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]['examples']
                    examples = [i['text'] for i in examples]
                except:
                    examples = ["No examples found..."]  

                context = {
                    'word' : word,
                    'definition' : definition,
                    'synonyms' : synonyms,
                    'examples' : examples,
                }
                return render(request, template_name="lookup.html", context=context)
        return render(request, template_name="lookup.html")
    
class Scraper(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            pass
        return render(request, template_name="scraper.html")