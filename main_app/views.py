from django.shortcuts import render

from django.http import HttpResponse
from .models import Movie

class Movie:
    def __init__(self, title, year, actors, genre):
        self.title = title
        self.year = year
        self.actors = actors
        self.genre = genre

 
movies = [
    Movie('The Replacements', '2000', 'Keanu Reeves', 'comedy'),
    Movie('The Matrix', '1999', 'Laurence Fishborne, Keanu Reeves', 'Action, Sci Fi, Fantasy'),
    Movie('Friday', '1995', 'Ice Cube, Chris Tucker, John Witherspoon', 'Comedy')
]



def home(request):
  return HttpResponse('<h1>Hello WOrld!!</h1>')

def about(request):
    return render(request, 'about.html')

def movies_index(request):
    return render(request, 'movies/index.html', { 'movies': movies })