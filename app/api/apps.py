from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = "api"

    def ready(self):
        from . import updater
        from .updater import import_data_to_redis

        # Import data once during start up
        import_data_to_redis()

        # Start the scheduler
        updater.start()
