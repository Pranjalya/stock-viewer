from django.apps import AppConfig
from .updater import start


class ApiConfig(AppConfig):
    name = "api"

    def ready(self):
        start()