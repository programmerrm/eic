#########################################
"""
ADMIN UI DESING SETUP
"""
#########################################
from django.contrib import admin
from faq.models import FaqTopBar, FaqSection, FaqItem

# REGISTER MODELS HERE.
admin.site.register(FaqTopBar)
admin.site.register(FaqSection)
admin.site.register(FaqItem)
