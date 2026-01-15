from django.urls import path
from .views import donation_proofs

urlpatterns = [
    path("donation/<int:donation_id>/proofs/", donation_proofs),
]
