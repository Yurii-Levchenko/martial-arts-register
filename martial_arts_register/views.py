from django.shortcuts import render, get_object_or_404
from .models import MartialArt
from django.http import Http404
from django.db.models import Avg


# Create your views here.
def index(request):
    martial_arts = MartialArt.objects.all().order_by("name")
    
    num_ma = martial_arts.count()
    avg_rating = martial_arts.aggregate(Avg("rating"))

    return render(request, "martial_arts_register/index.html", {
        "martial_arts": martial_arts,
        "total": num_ma,
        "average_rating": avg_rating
    })

def martial_art_detail(request, slug):
    martial_art = get_object_or_404(MartialArt, slug=slug)
    
    return render(request, "martial_arts_register/martial_art_detail.html", {
        "name": martial_art.name,
        "country_of_origin": martial_art.country_of_origin,
        "rating": martial_art.rating,
        "joint_locks_allowed": martial_art.joint_locks_allowed,
    })