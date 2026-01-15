from django.contrib import admin
from .models import Proof
from ngos.models import NGOTrust

@admin.register(Proof)
class ProofAdmin(admin.ModelAdmin):
    list_display = ("donation", "approved", "uploaded_at")
    list_filter = ("approved",)

    def save_model(self, request, obj, form, change):
        old_approved = False

        if obj.pk:
            old_approved = Proof.objects.get(pk=obj.pk).approved

        super().save_model(request, obj, form, change)

        # ✅ if admin just approved proof now (false -> true)
        if (old_approved == False) and (obj.approved == True):
            ngo = obj.donation.ngo
            trust, _ = NGOTrust.objects.get_or_create(ngo=ngo)

            trust.total_proofs_approved += 1
            trust.trust_score += 10   # ✅ rule: approved proof gives +10
            trust.save()
