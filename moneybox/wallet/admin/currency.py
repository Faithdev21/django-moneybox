from django.contrib import admin
from wallet.models.currency import Currency, CurrencyRate


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "updated_at", "code", "name")
    list_filter = ("created_at", "updated_at", "id", "code", "name")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "updated_at",
        "source_currency",
        "target_currency",
        "rate",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "source_currency",
        "target_currency",
        "id",
        "rate",
    )
    date_hierarchy = "created_at"
