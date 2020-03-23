from django.shortcuts import render, redirect
from django.views.generic import View
import requests
import time
import json
import webbrowser

class ResponseView(View):

    def get(self, request):
        if request.GET.get('dominio'):
            destination = 'http://'+request.GET['dominio']
            if request.GET.get('ip'):
                destination = 'http://'+request.GET['ip']
            before = time.time()
            r = requests.get(destination)
            responseTime = round((time.time() - before) * 1000)
            webbrowser.open_new_tab(destination)
            if r.history:
                print("Request was redirected")
                for resp in r.history:
                    print(resp.status_code, resp.url)
                    print("Final destination:\n{} {}".format(r.status_code, r.url))
                rdict = dict(status_code=r.history[0].status_code, time='{}ms'.format(responseTime))
            else:
                print("Request was not redirected")
                rdict = dict(status_code=r.status_code, time='{}ms'.format(responseTime))
            rjson = json.dumps(rdict)
            context = {
                'rjson': rjson,
                'destination': r.url
            }
            print(rjson)
            return render(request, 'home.html', context)
        else:
            return render(request, 'home.html')