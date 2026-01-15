from rest_framework import serializers
from .models import NGO, NGOTrust

class NGORegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NGO
        fields = [
            "id",
            "name",
            "darpan_id",
            "audit_number",
            "verification_status",
        ]
        read_only_fields = ["verification_status"]
class NGOTrustSerializer(serializers.ModelSerializer):
    ngo_name = serializers.CharField(source="ngo.name", read_only=True)

    class Meta:
        model = NGOTrust
        fields = ["ngo_name", "trust_score", "total_donations", "total_proofs_approved"]