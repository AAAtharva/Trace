@api_view(['POST'])
def add_fund_usage(request):
    donation = Donation.objects.get(id=request.data.get('donation_id'))

    FundUsage.objects.create(
        donation=donation,
        amount_used=request.data.get('amount_used'),
        purpose=request.data.get('purpose')
    )

    return Response(
        {"message": "Fund usage recorded"},
        status=status.HTTP_201_CREATED
    )

