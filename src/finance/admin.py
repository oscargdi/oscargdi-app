# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Account, Currency


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "created_at",
        "updated_at",
        "name",
        "currency",
        "balance",
    )
    list_filter = ("user", "created_at", "updated_at", "currency")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "created_at",
        "updated_at",
        "code",
        "symbol",
    )
    list_filter = ("user", "created_at", "updated_at")
    date_hierarchy = "created_at"
