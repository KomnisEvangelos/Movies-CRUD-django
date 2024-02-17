from django.urls import path
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.home, name=""),  # Home page
    path('about-us/', views.about_us, name="about-us"),  # About page
    path('browse/', views.browse, name="browse"),  # Browse page
    path('register/', views.register, name="register"),  # Register page
    path('admin-login/', views.admin_login, name="admin-login"),  # Login page
    path('admin-logout/', views.admin_logout, name="admin-logout"),  # Logout page
    path('dashboard/', views.dashboard, name="dashboard"),  # Dashboard page
    path('create-movie/', views.create_movie, name="create-movie"),
    path('update-movie/<int:pk>/', views.update_movie, name='update-movie'),
    path('movie/<int:pk>/', views.singular_movie, name="movie"),
    path('delete-movie/<int:pk>/', views.delete_movie, name="delete-movie"),
    path('create-director/', views.create_director, name="create-director"),
    path('update-director/<int:pk>/', views.update_director, name="update-director"),
    path('director/<int:pk>/', views.singular_director, name="director"),
    path('delete-director/<int:pk>/', views.delete_director, name="delete-director"),
    path('create-genre/', views.create_genre, name="create-genre"),
    path('update-genre/<int:pk>/', views.update_genre, name="update-genre"),
    path('genre/<int:pk>/', views.singular_genre, name="genre"),
    path('delete-genre/<int:pk>/', views.delete_genre, name="delete-genre"),
    path('movie-details/<int:pk>/', views.movie_details, name='movie-details'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)