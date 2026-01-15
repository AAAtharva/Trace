from django.urls import path, include

from donation import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/donation/", include("donation.urls")),
]
