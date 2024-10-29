from django.apps import AppConfig


class MyappConfig(AppConfig):
    """
    Configuration class for the 'myapp' application.

    Attributes:
        default_auto_field (str): The default auto field type for models.
        name (str): The name of the application.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "myapp"
