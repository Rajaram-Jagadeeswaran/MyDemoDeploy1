from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [ 
    #/movies/ 
    path('', views.index, name='index'),
    #/movies/ide.g./movies/1 
    path('<int:movie_id>/', views.show, name='show'),
    path('new/', views.new, name='new'),
    path('createmovie/', views.movie_create),
    path('<int:movie_id>/edit/', views.movie_update, name='edit'),
    path('<int:movie_id>/delete/', views.movie_delete, name='delete')
]
