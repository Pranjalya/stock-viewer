from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    get_stocks_by_prefix,
    get_all_stocks,
    get_stocks_by_search_query,
    download_csv,
    check_api
)

urlpatterns = {
    path(
        "stocks/page=<slug:page>&perPage=<slug:perPage>/", get_all_stocks, name="stocks"
    ),
    path(
        "stocks/prefix/name=<slug:name>&page=<slug:page>&perPage=<slug:perPage>/",
        get_stocks_by_prefix,
        name="stocks_by_prefix",
    ),
    path(
        "stocks/search/name=<slug:name>&page=<slug:page>&perPage=<slug:perPage>/",
        get_stocks_by_search_query,
        name="stocks_by_query",
    ),
    path("stocks/download/key=<slug:key>&text=<slug:text>/", download_csv, name="download_csv"),
    path("stocks/test/", check_api, name="check_api"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
