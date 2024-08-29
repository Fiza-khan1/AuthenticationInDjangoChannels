from django.apps import AppConfig


class ChannelappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ChannelApp'

    def ready(self):
        import ChannelApp.signals
