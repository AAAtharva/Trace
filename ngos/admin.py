from django.contrib import admin
from .models import NGO
from .models import Donor, Donation

@admin.register(NGO)
class NGOAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "darpan_id",
        "audit_number",
        "verification_status",
        "created_at",
    )

    list_filter = ("verification_status",)
    search_fields = ("name", "darpan_id")

admin.site.register(Donor)
admin.site.register(Donation)
