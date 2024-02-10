from http import HTTPStatus
from django.http import HttpResponse, JsonResponse

from arb_spotter_app.models import (
    MarketData,
    OneDayOhlcvData,
    OneHourOhlcvData,
    OneMinOhlcvData,
)

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from drf_yasg import openapi

candle_size_model_map = {
    "1m": OneMinOhlcvData,
    "1h": OneHourOhlcvData,
    "1d": OneDayOhlcvData,
}

user_response = openapi.Response("response description", "")
p_candle_size = openapi.Parameter(
    "candle_size",
    openapi.IN_QUERY,
    description="candle size",
    type=openapi.TYPE_STRING,
    enum=list(candle_size_model_map.keys()),
)
p_token = openapi.Parameter(
    "token",
    openapi.IN_QUERY,
    description="token symbol",
    type=openapi.TYPE_STRING,
)
p_exchange = openapi.Parameter(
    "exchange",
    openapi.IN_QUERY,
    description="exchange name",
    type=openapi.TYPE_STRING,
)


@swagger_auto_schema(method="get", operation_description="GET /tokens")
@api_view(["GET"])
def tokens(request):
    market_data = MarketData.objects.distinct("token")
    data = list(market_data.values())
    return JsonResponse(data={"data": data}, status=200)


@swagger_auto_schema(method="get", operation_description="GET /tokens/{token_id}")
@api_view(["GET"])
def token_details(request, token_id):
    market_data = MarketData.objects.filter(token_id=token_id)
    data = list(market_data.values())
    return JsonResponse(data={"data": data}, status=200)


@swagger_auto_schema(
    method="get",
    manual_parameters=[p_token, p_candle_size, p_exchange],
    operation_description="GET /history",
)
@api_view(["GET"])
def history(request):
    try:
        candle_size = request.GET["candle_size"]
        token = request.GET["token"]
        exchange = request.GET["exchange"]
    except:
        return HttpResponse(
            "missing query parameters, required 'candle_size', 'token', 'exchange'",
            status=HTTPStatus.BAD_REQUEST,
        )

    model = candle_size_model_map[candle_size]
    ohlcv = (
        model.objects.filter(token=token.upper(), exchange=exchange.lower())
        .order_by("updatedat")
        .values("open", "high", "close", "volume", "updatedat")
    )
    return JsonResponse(data={"data": list(ohlcv), "size": len(ohlcv)}, status=200)
