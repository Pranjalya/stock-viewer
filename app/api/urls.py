from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import manage_items, manage_item, get_stocks, get_stock_by_prefix

urlpatterns = {
    path("stocks/", get_stocks, name="stocks"),
    path("stocks/<slug:name>/", get_stock_by_prefix, name="stocks_by_name")
}

urlpatterns = format_suffix_patterns(urlpatterns)
