from django.apps import AppConfig

class AboutPageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about_page'
    verbose_name = 'About Page'

    def ready(self):
        import about_page.signals
