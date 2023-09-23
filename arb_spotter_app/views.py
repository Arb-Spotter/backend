from http import HTTPStatus
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from arb_spotter_app.models import Exchanges, MarketData, OneDayOhlcvData, OneHourOhlcvData, OneMinOhlcvData

# Create your views here.

candle_size_model_map = {
    "1m": OneMinOhlcvData,
    "1h": OneHourOhlcvData,
    "1d": OneDayOhlcvData
}


def tokens(request):
    market_data = MarketData.objects.distinct('token')
    data = list(market_data.values())
    return JsonResponse(data={"data": data}, status= 200)
    

def token_details(request, token_id):
    market_data = MarketData.objects.filter(token_id=token_id)
    data = list(market_data.values())
    return JsonResponse(data={"data": data}, status= 200)


def history(request):
    try:

        candle_size = request.GET['candle_size']
        token = request.GET['token']
        exchange = request.GET['exchange']
    except:
        return HttpResponse("missing query parameters, required 'candle_size', 'token', 'exchange'", status=HTTPStatus.BAD_REQUEST)

    model = candle_size_model_map[candle_size]
    ohlcv = model.objects.filter(token=token, exchange=exchange).order_by("updatedat").values("close", "updatedat")
    return JsonResponse(data={"data": list(ohlcv)}, status= 200)