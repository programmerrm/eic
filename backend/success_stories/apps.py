from django.apps import AppConfig

class SuccessStoriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'success_stories'
    verbose_name = "Case Studies Page"

    def ready(self):
        import success_stories.signals
