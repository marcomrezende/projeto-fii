from __future__ import unicode_literals
from django.db.models import JSONField
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import UniqueConstraint, Q


class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True,
        verbose_name=_('Id')
    )
    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        null=True,
        verbose_name=_('Created at')
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified',
        auto_now=True,
        null=True,
        verbose_name=_('Modified at')
    )
    active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True,
        verbose_name=_('Active'),
    )

    class Meta:
        abstract = True
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view')


class AtivosDividendos(ModelBase):
    ticket = models.CharField(
        max_length=8
    )
    dividendo = models.DecimalField(
        max_digits=3,
        decimal_places=2
    )

    class Meta:
        db_table = 'ativos_dividendos'
        verbose_name = _('AtivosDividendos')


