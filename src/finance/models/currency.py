from django.db import models
from .base import BaseModel


class Currency(BaseModel):
    code = models.CharField(max_length=10)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.name
