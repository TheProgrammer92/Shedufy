from django.apps import AppConfig


class MyresourcesConfig(AppConfig):
    name = 'myresources'

    def ready(self):
        import myresources.signals
