from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Movie, Director, Genre
# - Register user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1','password2']


# - Login User
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

#Creat Movie
class CreateMovieForm(forms.ModelForm):

    class Meta:

        model = Movie
        fields = ['title', 'length', 'genre', 'premiere', 'imbd_url', 'imdb_score', 'short_desc', 'director', 'review', 'site_score','poster']
        widgets = {
            'poster': forms.FileInput(attrs={'accept': 'image/*'}),
        }

# - Update Movie

class UpdateMovieForm(forms.ModelForm):

    class Meta:

        model = Movie
        fields = ['title', 'length', 'genre', 'premiere', 'imbd_url', 'imdb_score', 'short_desc', 'director', 'review', 'site_score','poster']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['genre_name']

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['director_name']