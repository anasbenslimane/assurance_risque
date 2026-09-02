from django.contrib import admin
from .models import PredictionHistory

admin.site.site_header = "Assurance Anas - Administration"
admin.site.site_title = "Assurance Anas"
admin.site.index_title = "Panneau d'administration"

@admin.register(PredictionHistory)
class PredictionHistoryAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "prediction",
        "risk_level",
        "claim_probability",
        "Region",
        "VehBrand",
        "DrivAge",
    )

    list_filter = (
        "prediction",
        "risk_level",
        "Region",
        "VehBrand",
    )

    search_fields = (
        "Region",
        "VehBrand",
    )

    ordering = ("-created_at",)