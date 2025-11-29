from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

# ========= ABOUT TOP BAR =================
class AboutTopBar(models.Model):
    title = models.CharField(
        max_length=280,
        verbose_name=_('Title'),
        help_text=_('Enter your about section top bar title...')
    )
    description = models.TextField(
        verbose_name=_('Description'),
        help_text=('Enter your about section top bar description...')
    )

    class Meta:
        verbose_name = 'About Top Bar'
        verbose_name_plural = _('About Top Bar')

    def __str__(self):
        return f"About top bar data infomation added."
    

    