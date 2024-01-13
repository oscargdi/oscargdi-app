from django.db import models
from .base import BaseModel


class Account(BaseModel):
    name = models.CharField(max_length=100)
    currency = models.ForeignKey("Currency", on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.name
