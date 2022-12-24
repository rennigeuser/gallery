from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class CreatedAtUpdatedAtByMixin(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        verbose_name=_('Author')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name=_('Creation date'),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
        verbose_name=_('Date of update'),
    )

    class Meta:
        abstract = True


class DragAndDropOrderingMixin(models.Model):
    order_by = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        abstract = True
