from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import json
from django.conf import settings
import redis
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import csv

# Connect to our Redis instance
redis_instance = redis.StrictRedis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0, decode_responses=True, password=settings.REDIS_PASSWORD
)


@api_view(["GET"])
def get_stocks_by_prefix(request, *args, **kwargs):
    if request.method == "GET":
        if kwargs.get("name", 0):
            items = []
            count = 0
            prefix = kwargs["name"].upper()
            match = prefix + "*"

            page = int(kwargs.get("page", "1"))
            perPage = int(kwargs("perPage", "10"))

            startIndex = (page - 1) * perPage
            endIndex = page * perPage

            for key in redis_instance.scan_iter(match=match):
                items.append(redis_instance.hgetall(key))
                count += 1

            items.sort(key=lambda x: x['SC_NAME'])

            if len(items) == 0 or startIndex > count:
                response = {"key": kwargs["name"],
                            "value": None, "msg": "Not found"}
                return Response(response, status=404)
            else:
                response = {
                    "count": count,
                    "msg": f"Found {count} items.",
                    "items": items[startIndex:endIndex],
                }
                return Response(response, status=200)


@api_view(["GET"])
def get_stocks_by_search_query(request, *args, **kwargs):
    if request.method == "GET":
        if kwargs.get("name", 0):
            items = []
            count = 0
            prefix = kwargs.get("name", "*").upper()
            match = "*" + prefix + "*"

            page = int(kwargs.get("page", "1"))
            perPage = int(kwargs("perPage", "10"))

            startIndex = (page - 1) * perPage
            endIndex = page * perPage

            for key in redis_instance.scan_iter(match=match):
                items.append(redis_instance.hgetall(key))
                count += 1

            items.sort(key=lambda x: x['SC_NAME'])

            if len(items) == 0 or startIndex > count:
                response = {"key": kwargs["name"],
                            "value": None, "msg": "Not found"}
                return Response(response, status=404)
            else:
                response = {
                    "count": count,
                    "msg": f"Found {count} items.",
                    "items": items[startIndex:endIndex],
                }
                return Response(response, status=200)


@api_view(["GET"])
def get_all_stocks(request, *args, **kwargs):
    if request.method == "GET":
        items = []
        count = 0

        page = int(kwargs.get("page", "1"))
        perPage = int(kwargs("perPage", "10"))

        for key in redis_instance.scan_iter("*"):
            items.append(redis_instance.hgetall(key))
            count += 1

        items.sort(key=lambda x: x['SC_NAME'])

        startIndex = (page - 1) * perPage
        endIndex = page * perPage

        if len(items) == 0 or startIndex > count:
            response = {"value": None, "msg": "Not found"}
            return Response(response, status=404)
        else:
            response = {
                "count": count,
                "msg": f"Found {count} items.",
                "items": items[startIndex:endIndex],
            }
            return Response(response, status=200)


@api_view(["GET"])
def download_csv(request, *args, **kwargs):
    if request.method == "GET":
        if kwargs.get("key", 0):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="export.csv"'
            writer = csv.DictWriter(response, fieldnames=[
                                    'SC_CODE', 'SC_NAME', 'OPEN', 'CLOSE', 'HIGH', 'LOW'])
            writer.writeheader()

            items = []

            row = None

            if kwargs["key"] == "all":
                match = "*"
            elif kwargs["key"] == "prefix":
                match = kwargs["text"].upper() + \
                    "*" if kwargs.get("text", None) != None else "*"
            elif kwargs["key"] == "fulltext":
                match = "*" + kwargs["text"].upper() + \
                    "*" if kwargs.get("text", None) != None else "*"

            for key in redis_instance.scan_iter(match=match):
                row = redis_instance.hgetall(key)
                writer.writerow(row)

            if not row:
                response = {"key": kwargs["key"],
                            "value": None, "msg": "Not found"}
                return Response(response, status=404)

            return response

@api_view(["GET"])
def check_api(request, *args, **kwargs):
    if request.method == "GET":
        return Response({"ans": 2}, status=200)
