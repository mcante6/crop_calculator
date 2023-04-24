from django.apps import AppConfig

class CalculationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'calculations'

    def ready(self):
        import calculations.templatetags.dict_filters
