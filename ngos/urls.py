

from django.urls import path
from .views import register_ngo, ngo_status, donate, ngo_donation
from .views import leaderboard ,donor_donations, add_fund_usage

urlpatterns = [
    path("register/", register_ngo),
    path("status/<str:darpan_id>/", ngo_status),

    path("donate/", donate),
    path("ngo/<int:ngo_id>/donation/", ngo_donation),
    path("leaderboard/", leaderboard),
    path("donor/<str:email>/donations/", donor_donations),
    path("fund-usage/add/", add_fund_usage),
]


