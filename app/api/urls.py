from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import manage_items, manage_item, get_stocks

urlpatterns = {
    path("", manage_items, name="items"),
    path("<slug:key>", manage_item, name="single_item"),
    path("stocks/", get_stocks, name="stocks"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
