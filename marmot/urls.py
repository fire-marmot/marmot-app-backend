from django.urls import path
from .views import MoviesList, MoviesDetail, UserList,UserDetail

urlpatterns = [
    path("", MoviesList.as_view(), name="movies_list"),
    path("<int:pk>/", MoviesDetail.as_view(), name="movies_detail"),
    path("user", UserList.as_view(), name="user_list"),
    path("user/<int:pk>/", UserDetail.as_view(), name="user_detail"),
]
