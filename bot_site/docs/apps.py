from django.apps import AppConfig

class DocsConfig(AppConfig):
    name = 'docs'

    def ready(self):
        import docs.signals
