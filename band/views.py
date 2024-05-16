from django.shortcuts import render
from .models import Band

def band_listing(request):
    """A view of all bands."""
    bands = Band.objects.all()
    return render(request, "bands/band_listing.html", {"bands": bands})
