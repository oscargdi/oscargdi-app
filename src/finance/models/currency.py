from django.db import models
from .base import BaseModel
from django.utils.translation import gettext_lazy as _


class Currency(BaseModel):
    code = models.CharField(max_length=10)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name_plural = _("currencies")
