from django.db import models
# from donation.models import Donation
# Donation.objects.all()
class Donation(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amount)
        return f"Donation {self.id}"

