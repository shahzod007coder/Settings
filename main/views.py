from django.shortcuts import render
from main.models import Categoriya, Post, Product


def index(request):
    categoriya = Categoriya.objects.all()
    ctx = {
        'categoriya': categoriya
    }
    return render(request, "main/index.html", ctx)
