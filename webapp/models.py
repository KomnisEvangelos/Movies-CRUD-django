from django.db import models

class Director(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    director_name = models.CharField(max_length=100)
   
class Movie(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    length = models.DecimalField(decimal_places=1,max_digits=3)
    genre = models.CharField(max_length=100)
    premiere = models.DateField()
    imbd_url = models.CharField(max_length=100)
    imdb_score = models.DecimalField(decimal_places=1,max_digits=3)
    short_desc = models.CharField(max_length=100)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    review = models.CharField(max_length=1000)
    site_score = models.DecimalField(decimal_places=1,max_digits=3)
    poster = models.ImageField(upload_to='movie_photos/', null=True, blank=True)

class Genre(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    genre_name = models.CharField(max_length=100)

