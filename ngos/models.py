
from django.db import models

class NGO(models.Model):
    name = models.CharField(max_length=200)
    cause = models.CharField(max_length=100)

    # Identity
    darpan_id = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    audit_number = models.CharField(
    max_length=100,
    null=True,
    blank=True
)

    # Verification status (STATE, not boolean)
    verification_status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("verified", "Verified"),
            ("rejected", "Rejected"),
        ],
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Donor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Donation(models.Model):
    donor = models.ForeignKey(
        Donor,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Donation"
        verbose_name_plural = "Donation"
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE)

    amount = models.IntegerField()
    used_amount = models.IntegerField(default=0)

    status = models.CharField(
        max_length=20,
        choices=[
            ("received", "Received"),
            ("in_use", "In Use"),
            ("completed", "Completed"),
            ("refunded", "Refunded"),
        ],
        default="received"
    )
    def remaining_amount(self):
        return self.amount - self.used_amount

    def __str__(self):
        return f"Donation {self.id} - ₹{self.amount}"
    created_at = models.DateTimeField(auto_now_add=True)

class FundUsage(models.Model):
    donation = models.ForeignKey(
        'donation.Donation', 
        on_delete=models.CASCADE
        )
    amount_used = models.DecimalField(max_digits=10, decimal_places=2)
    purpose = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount_used} used from Donation {self.donation.id}"
class NGOTrust(models.Model):
    ngo = models.OneToOneField(NGO, on_delete=models.CASCADE)
    trust_score = models.IntegerField(default=0)
    total_donations = models.IntegerField(default=0)
    total_proofs_approved = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.ngo.name} - Trust {self.trust_score}"

