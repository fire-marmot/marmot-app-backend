from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Movies, User, Watched, Genres, Reviews, Service
from .permissions import IsOwnerOrReadOnly
from .serializers import MoviesSerializer, UserSerializer, WatchedSerializer,GeneresSerializer, ReviewsSerializer, ServiceSerializer


class MoviesList(ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer


class MoviesDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WatchedList(ListCreateAPIView):
    queryset = Watched.objects.all()
    serializer_class = WatchedSerializer


class WatchedDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Watched.objects.all()
    serializer_class = WatchedSerializer

class GenresList(ListCreateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GeneresSerializer


class GenresDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Genres.objects.all()
    serializer_class = GeneresSerializer

class ReviewsList(ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


class ReviewsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

class ServiceList(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ReviewsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Service.objects.all()
    serializer_class =  ServiceSerializer

