#########################################
"""
ADMIN UI DESING SETUP
"""
#########################################
from django.contrib import admin
from success_stories.models import SuccessStorieTopBar, SuccessStorieCategory, SuccessStorie, SeoTag, Schema

# REGISTER MODELS HERE.
admin.site.register(SuccessStorieTopBar)
admin.site.register(SuccessStorieCategory)
admin.site.register(SuccessStorie)
admin.site.register(SeoTag)
admin.site.register(Schema)
