from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import get_stock_by_prefix, get_all_stocks

urlpatterns = {
    path("stocks/page=<slug:page>&perPage=<slug:perPage>/", get_all_stocks, name="stocks"),
    path(
        "stocks/name=<slug:name>&page=<slug:page>&perPage=<slug:perPage>/",
        get_stock_by_prefix,
        name="stocks_by_name",
    ),
}

urlpatterns = format_suffix_patterns(urlpatterns)
