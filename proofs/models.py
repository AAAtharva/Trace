from django.db import models

class Proof(models.Model):
    donation = models.ForeignKey(
        'ngos.Donation',   
        on_delete=models.CASCADE,
        related_name='proofs'
    )
    image = models.ImageField(upload_to='proofs/')
    description = models.TextField(blank=True, null=True)  # ✅ ADD THIS

    approved = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Proof for Donation {self.donation.id}"
# from django.db import models
# from ngos.models import NGO
# from donation.models import Donation

# class Proof(models.Model):
#     PROOF_TYPE_CHOICES = [
#         ('photo', 'Photo'),
#         ('video', 'Video'),
#         ('bill', 'Bill'),
#     ]

#     ngo = models.ForeignKey(NGO, on_delete=models.CASCADE)
#     donation = models.ForeignKey("ngos.Donation", on_delete=models.CASCADE)
#     proof_type = models.CharField(max_length=10, choices=PROOF_TYPE_CHOICES)
#     file = models.FileField(upload_to='proofs/')
#     description = models.TextField(blank=True)
#     approved = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#          return f"Proof for Donation {self.donation.id}"
         
#          return f"{self.proof_type} - {self.ngo.name}"