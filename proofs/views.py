from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Proof
from ngos.models import NGO
from donation.models import Donation

@api_view(['POST'])
def upload_proof(request):
    ngo = NGO.objects.get(id=request.data.get('ngo_id'))
    donation = Donation.objects.get(id=request.data.get('donation_id'))

    proof = Proof.objects.create(
        ngo=ngo,
        donation=donation,
        proof_type=request.data.get('proof_type'),
        file=request.FILES.get('file'),
        description=request.data.get('description')
    )

    return Response(
        {"message": "Proof uploaded, pending approval"},
        status=status.HTTP_201_CREATED
    )
from .models import Proof

@api_view(["GET"])
def donation_proofs(request, donation_id):
    proofs = Proof.objects.filter(donation_id=donation_id, approved=True)

    data = []
    for p in proofs:
        data.append({
            "proof_id": p.id,
            "image": p.image.url if p.image else None,
            "approved": p.approved,
            "uploaded_at": p.uploaded_at
        })

    return Response(data)