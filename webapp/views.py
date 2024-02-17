from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, LoginForm, CreateMovieForm, UpdateMovieForm
from .forms import GenreForm, DirectorForm
from .models import Genre, Director, Movie 

from django.contrib import messages

def home(request):
    return render(request, 'webapp/index.html')

def about_us(request):
    return render(request, 'webapp/about-us.html')

def browse(request):
    movies = Movie.objects.all().order_by('title')
    genres = Genre.objects.all()
    directors = Director.objects.all()

    category = request.GET.get('category')
    if category:
        movies = movies.filter(genre=category)

    director = request.GET.get('director')
    if director:
        movies = movies.filter(director__director_name=director)
        
    return render(request, 'webapp/browse.html', {'movies': movies, 'genres':genres,'directors':directors})

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-login')
    

    context = {'form':form}
    return render(request, 'webapp/register.html', context=context)


def admin_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data =request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
    
    context = {'form':form}

    return render(request, 'webapp/admin-login.html',context=context)

def admin_logout(request):
   auth.logout(request)
   return redirect('admin-login')

@login_required(login_url='admin-login')
def  dashboard(request):
    all_movies = Movie.objects.all()
    all_directors = Director.objects.all()
    all_genres = Genre.objects.all()
    context = {
        'movies': all_movies,
        'directors': all_directors,
        'genres': all_genres,
    }

    return render(request,'webapp/dashboard.html',context=context)


@login_required(login_url='admin-login')
def create_movie(request):

    form = CreateMovieForm()

    if request.method == "POST":

        form = CreateMovieForm(request.POST,request.FILES)

        if form.is_valid():

            form.save()

            messages.success(request, "Your Movie was created!")

            return redirect("dashboard")

    genres = Genre.objects.all()
    directors = Director.objects.all()

    context = {'form': form, 'genres': genres, 'directors': directors}

    return render(request, 'webapp/create-movie.html', context=context)


@login_required(login_url='admin-login')
def update_movie(request, pk):

    try:
        movie = Movie.objects.get(id=pk)
    except Movie.DoesNotExist:
        movie = None

    genres = Genre.objects.all()
    directors = Director.objects.all()

    form = UpdateMovieForm(instance=movie)

    if request.method == 'POST':

        form = UpdateMovieForm(request.POST, instance=movie)

        if form.is_valid():

            form.save()

            messages.success(request, "Your Movie was updated!")

            return redirect("dashboard")
        
    context = {'form':form, 'genres':genres, 'directors':directors}

    return render(request, 'webapp/update-movie.html', context=context)


@login_required(login_url='admin-login')
def singular_movie(request, pk):

    all_movies = Movie.objects.get(id=pk)

    context = {'movie':all_movies}

    return render(request, 'webapp/view-movie.html', context=context)


@login_required(login_url='admin-login')
def delete_movie(request, pk):

    movie = Movie.objects.get(id=pk)

    movie.delete()

    messages.success(request, "Your Movie was deleted!")

    return redirect("dashboard")

# Create
def create_genre(request):
    form = GenreForm()
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Genre created successfully.')
            return redirect('dashboard')
    return render(request, 'webapp/create-genre.html', {'form': form})

def create_director(request):
    form = DirectorForm()
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Director created successfully.')
            return redirect('dashboard')
    return render(request, 'webapp/create-director.html', {'form': form})


# Update
def update_genre(request, pk):
    genre = Genre.objects.get(id=pk)

    form = GenreForm(instance=genre)
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            messages.success(request, 'Genre updated successfully.')
            return redirect('dashboard')
    return render(request, 'webapp/update-genre.html', {'form': form})

def update_director(request, pk):
    director = Director.objects.get(id=pk)
    form = DirectorForm(instance=director)
    if request.method == 'POST':
        form = DirectorForm(request.POST, instance=director)
        if form.is_valid():
            form.save()
            messages.success(request, 'Director updated successfully.')
            return redirect('dashboard')
    return render(request, 'webapp/update-director.html', {'form': form})

# Delete
def delete_genre(request, pk):
    genre = Genre.objects.get(pk=pk)
    
    genre.delete()
    messages.success(request, 'Genre deleted successfully.')
    return redirect('dashboard')

def delete_director(request, pk):
    director = Director.objects.get(id=pk)
    
    director.delete()
    messages.success(request, 'Director deleted successfully.')
    return redirect('dashboard')

@login_required(login_url='admin-login')
def singular_director(request, pk):

    all_movies = Director.objects.get(id=pk)

    context = {'director':all_movies}

    return render(request, 'webapp/view-director.html', context=context)

@login_required(login_url='admin-login')
def singular_genre(request, pk):

    all_movies = Genre.objects.get(id=pk)

    context = {'genre':all_movies}

    return render(request, 'webapp/view-genre.html', context=context)

def movie_details(request, pk):
    movie = Movie.objects.get(id=pk)
    return render(request, 'webapp/movie_details.html', {'movie': movie})