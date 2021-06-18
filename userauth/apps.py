from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'userauth'

    def ready(self):
        import userauth.signals


