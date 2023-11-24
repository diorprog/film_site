from pyexpat.errors import XML_ERROR_RECURSIVE_ENTITY_REF

from django.shortcuts import render, redirect

from main.models import Premier, Popular, Recent, Film, Tv, Comment, Hero, Review


def home(request):
    premier = Premier.objects.all()[:6]
    popular = Popular.objects.all()[:6]
    recent = Recent.objects.all()[:6]
    film = Film.objects.all()[:6]
    tv = Tv.objects.all()[:6]
    comment = Comment.objects.all()[:6]
    hero = Hero.objects.all()
    review = Review.objects.all()
    return render(request, "index.html", {
        'premier': premier,
        'popular': popular,
        'recent': recent,
        'film': film,
        'tv': tv,
        'comment': comment,
        'hero': hero,
        'review': review
    })


def categories(request):
    return render(request, "categories.html")


def amime_details(request):
    return render(request, "anime-details.html")


def anime_watching(request):
    return render(request, "anime-watching.html")


def blog(request):
    return render(request, "blog.html")


def login(request):
    return render(request, "login.html")


def blog_details(request):
    return render(request, "blog-details.html")


def register(request):
    return render(request, "register.html")


def contacts(request):
    return render(request, "contacts.html")

