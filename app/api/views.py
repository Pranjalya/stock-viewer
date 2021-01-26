from django.shortcuts import render

# Create your views here.
import json
from django.conf import settings
import redis
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Connect to our Redis instance
redis_instance = redis.StrictRedis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=1, decode_responses=True
)

@api_view(["GET"])
def get_stocks(request, *args, **kwargs):
    if request.method == "GET":
        items = {}
        count = 0
        for key in redis_instance.keys("*"):
            items[key] = redis_instance.hgetall(key)
            count += 1
        response = {"count": count, "msg": f"Found {count} items.", "items": items}
        return Response(response, status=200)


@api_view(["GET"])
def get_stock_by_prefix(request, *args, **kwargs):
    if request.method == "GET":
        if kwargs["name"]:
            items = {}
            count = 0
            prefix = kwargs["name"].upper()
            match = prefix + "*"
            for key in redis_instance.scan_iter(match=match):
                items[key] = redis_instance.hgetall(key)
                count += 1
            if len(items) == 0:
                response = {"key": kwargs["key"], "value": None, "msg": "Not found"}
                return Response(response, status=404)
            else:
                response = {"count": count, "msg": f"Found {count} items.", "items": items}
                return Response(response, status=200)
