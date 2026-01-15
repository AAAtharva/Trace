from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import NGORegisterSerializer
from .models import Donor, Donation, NGO, FundUsage
from .models import NGOTrust
from .serializers import NGOTrustSerializer
from proofs.models import Proof



@api_view(["POST"])
def donate(request):
    data = request.data

    required = ["donor_name", "email", "ngo_id", "amount"]
    for field in required:
        if not data.get(field):
            return Response({"error": f"{field} is required"}, status=400)

    try:
        ngo = NGO.objects.get(id=data["ngo_id"], verification_status="verified")
    except NGO.DoesNotExist:
        return Response({"error": "NGO not verified or not found"}, status=400)

    donor, _ = Donor.objects.get_or_create(
        email=data["email"],
        defaults={"name": data["donor_name"]}
    )

    donation = Donation.objects.create(
        donor=donor,
        ngo=ngo,
        amount=data["amount"]
    )

    return Response({
        "message": "Donation recorded",
        "donation_id": donation.id,
        "ngo": ngo.name,
        "amount": donation.amount,
        "status": donation.status
    })


    
@api_view(['POST'])
def register_ngo(request):
    data = request.data

    required_fields = ["name", "cause", "darpan_id", "audit_number"]
    for field in required_fields:
        if not data.get(field):
            return Response(
                {"error": f"{field} is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

    ngo = NGO.objects.create(
        name=data.get("name"),
        cause=data.get("cause"),
        darpan_id=data.get("darpan_id"),
        audit_number=data.get("audit_number"),
        verification_status="pending"
    )

    return Response(
        {
            "message": "NGO registered successfully",
            "verification_status": ngo.verification_status
        },
        status=status.HTTP_201_CREATED
    )

@api_view(['GET'])
def ngo_status(request, darpan_id):
    try:
        ngo = NGO.objects.get(darpan_id=darpan_id)
        return Response({
            "name": ngo.name,
            "verification_status": ngo.verification_status
        })
    except NGO.DoesNotExist:
        return Response(
            {"error": "NGO not found"},
            status=status.HTTP_404_NOT_FOUND
        )

def ngo_donation(request, ngo_id):
    donation = Donation.objects.filter(ngo_id=ngo_id)

    data = []
    for d in donation:
        data.append({
            "donor": d.donor.name,
            "amount": d.amount,
            "used": d.used_amount,
            "remaining": d.remaining_amount(),
            "status": d.status
        })

    return Response(data)

def ngo_proofs(request, ngo_id):
    proofs = Proof.objects.filter(ngo_id=ngo_id, approved=True)
    data = [
        {
            "type": p.proof_type,
            "file": p.file.url,
            "description": p.description
        }
        for p in proofs
    ]
    return Response(data)

from django.http import JsonResponse
from .models import NGOTrust

def leaderboard(request):
    trusts = NGOTrust.objects.all().order_by("-trust_score")

    data = []
    for t in trusts:
        data.append({
            "ngo_name": t.ngo.name,
            "trust_score": t.trust_score,
            "total_donations": t.total_donations,
            "total_proofs_approved": t.total_proofs_approved
        })

    return JsonResponse(data, safe=False)

from django.http import JsonResponse
from .models import Donor, Donation

def donor_donations(request, email):
    try:
        donor = Donor.objects.get(email=email)
    except Donor.DoesNotExist:
        return JsonResponse({"error": "Donor not found"}, status=404)

    donations = Donation.objects.filter(donor=donor).order_by("-created_at")

    data = []
    for d in donations:
        data.append({
            "donation_id": d.id,
            "ngo": d.ngo.name,
            "amount": d.amount,
            "used_amount": d.used_amount,
            "remaining": d.remaining_amount(),
            "status": d.status,
            "date": str(d.created_at),
        })

    return JsonResponse(data, safe=False)
def add_fund_usage(request):
    donation_id = request.data.get("donation_id")
    amount_used = request.data.get("amount_used")
    purpose = request.data.get("purpose")

    if not donation_id or not amount_used or not purpose:
        return Response(
            {"error": "donation_id, amount_used, purpose are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        donation = Donation.objects.get(id=donation_id)
    except Donation.DoesNotExist:
        return Response(
            {"error": "Donation not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    # ✅ create fund usage entry
    fund_usage = FundUsage.objects.create(
        donation=donation,
        amount_used=amount_used,
        purpose=purpose
    )

    # ✅ optional: update used_amount inside Donation
    donation.used_amount += int(amount_used)
    donation.save()

    return Response(
        {
            "message": "Fund usage recorded ✅",
            "fund_usage_id": fund_usage.id,
            "donation_id": donation.id,
            "used_amount_total": donation.used_amount
        },
        status=status.HTTP_201_CREATED
    )
