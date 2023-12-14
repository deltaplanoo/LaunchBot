from django.urls import path
from . import views

# used to map urls to view functions
# path(route, view)

# URLconf
urlpatterns = [
    path('', views.index, name='index'),
    path('upcoming', views.upcoming, name='upcoming'),
    path('past', views.past, name='past'),
    path('spacex', views.spacex, name='spacex'),
    path('starship', views.starship, name='starship'),
]
