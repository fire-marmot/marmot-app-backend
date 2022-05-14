from django.urls import path
from .views import MoviesList, MoviesDetail

urlpatterns = [
    path("", MoviesList.as_view(), name="movies_list"),
    path("<int:pk>/", MoviesDetail.as_view(), name="movies_detail"),
]
