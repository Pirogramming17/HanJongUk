from shutil import move
from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def home(request):
    movies = Movie.objects.all()
    context={
        "movies":movies
    }

    return render(request, template_name="posts/home.html", context=context)

def create(request):
    if request.method =="POST":
        title = request.POST["title"]
        director = request.POST["director"]
        main = request.POST["main"]
        years = request.POST["years"]
        genre = request.POST["genre"]
        starRating = request.POST["starRating"]
        runningTime = request.POST["runningTime"]
        reviews = request.POST["reviews"]

        Movie.objects.create(title=title, director=director, main=main, years=years, genre=genre, starRating=starRating, runningTime=runningTime, reviews=reviews)
        return redirect("/")
    context={

    }

    return render(request, template_name="posts/create.html", context=context)

def detail(request, id):
    movie = Movie.objects.get(id=id)
    context={"movie":movie}
    return render(request, template_name="posts/detail.html", context=context)

def update(request, id):
    if request.method == "POST":
        title = request.POST["title"]
        director = request.POST["director"]
        main = request.POST["main"]
        years = request.POST["years"]
        genre = request.POST["genre"]
        starRating = request.POST["starRating"]
        runningTime = request.POST["runningTime"]
        reviews = request.POST["reviews"]

        Movie.objects.filter(id=id).update(title=title, director=director,
        main=main, years=years, genre=genre, starRating=starRating, runningTime=runningTime,
        reviews=reviews)
        return redirect("/")

    elif request.method == "GET":
        movie = Movie.objects.get(id=id)
        context={"movie":movie}
        return render(request, template_name="posts/update.html", context=context)

def delete(request, id):
    if request.method == "POST":
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect("/")