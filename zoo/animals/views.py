from django.shortcuts import render
from .models import Animals


def index_view(request):
    animals = Animals.objects.all()
    return render(request, "animals/index.html", {'animals': animals})
