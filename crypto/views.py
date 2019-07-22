from django.shortcuts import render
import requests
import json


# Create your views here.
def home(request):

    # Grab crypto values
    api_request = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD")
    price = json.loads(api_request.content)

    # Grab cryto datas
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    news = json.loads(api_request.content)
    return render(request, 'home.html', context={'news': news, 'price': price})
