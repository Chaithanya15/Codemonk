from django.apps import AppConfig
# Configuration class for the 'core' application

class CoreConfig(AppConfig):
     # Set the default auto field type for primary keys
    default_auto_field = 'django.db.models.BigAutoField'
    # Define the name of the application
    name = 'core'
