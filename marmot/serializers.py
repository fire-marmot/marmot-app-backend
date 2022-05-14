from rest_framework import serializers
from .models import Movies,User,Watched,Genres,Reviews,Service


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class WatchedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watched
        fields = "__all__"

class GeneresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = "__all__"

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = "__all__"

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"