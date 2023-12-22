from django.apps import AppConfig
from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'auth_app'

    def ready(self):
        import auth_app.signals

