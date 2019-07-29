from django.shortcuts import render
import requests
import json


# Create your views here.
def home(request):
    # Grab crypto Price Data
    price_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,BCH,EOS,LTC,XLM,ADA,USDT,"
        "TRX&tsyms=USD,EUR")
    price = json.loads(price_request.content)

    # Grab cryto datas
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    news = json.loads(api_request.content)
    return render(request, 'home.html', context={'news': news, 'price': price})


def prices(request):
    if request.method == 'POST':
        quote = request.POST['quote']
        quote = quote.upper()
        price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+quote+"&tsyms=USD")
        price = json.loads(price_request.content)
        return render(request, 'prices.html', {'price': price})
    else:
        notfound = "Enter a crypto value on the search"
        return render(request, 'prices.html', {'notfound': notfound})
