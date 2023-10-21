from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.urls import reverse

from .models import Movie
from .forms import MovieForm  # Import the MovieForm class from your forms module

def index(request):
    newest_movies = Movie.objects.order_by('-release_date')[:15]
    context = {'newest_movies': newest_movies}
    return render(request, 'movies/index.html', context)
    
def show(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, 'movies/show.html', {'movie': movie})
    
def new(request):
   return render(request, 'movies/movie_create.html', {'form': MovieForm})
   
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect('/movies')  # Redirect to the movie details page
    else:
        form = MovieForm()
        form.save()
    return render(request, 'movies/movie_create.html', {'movie': form})

def movie_update(request, movie_id):
    
    movie = get_object_or_404(Movie, pk=movie_id)
    
    if request.method == 'POST':
        
        form = MovieForm(request.POST, instance=movie)
        
        if form.is_valid():
            form.save()
            return redirect('/movies')
    else:
        form = MovieForm(instance=movie)
        
    return render(request, 'movies/movie_form.html', {'form': form, 'movie': movie})

def movie_delete(request, movie_id):
    
    movie = get_object_or_404(Movie, pk=movie_id)
    
    if request.method == 'POST':
        movie.delete()
        return redirect('/movies')
    return render(request, 'movies/movie_confirm_delete.html', {'movie': movie})