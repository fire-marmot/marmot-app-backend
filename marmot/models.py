from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Movies(models.Model):
    title = models.CharField(max_length=256)
    movieID = models.CharField(max_length=500)
    streaming_service = models.CharField(max_length=500)
    average_rating = models.IntegerField(default=0)
    streaming_url = models.URLField()
    image_url = models.URLField()
    description = models.TextField(default="", null=True, blank=True)
    genre = models.IntegerField(default=0)
    # reviewID = models.ManyToManyField(Reviews)

    def __str__(self):
        return self.title


##User = User in our app
class User(models.Model):
    userID = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    liked = ArrayField(models.CharField(max_length=30), blank=True, null=True)
    watched = ArrayField(models.CharField(max_length=30), blank=True, null=True)


    def __str__(self):
        return self.first_name



class Watched(models.Model):

    watched = models.ManyToManyField(Movies)

    def __str__(self):
        return self.watched



class Genres(models.Model):
    genre_name = models.CharField(max_length=50)
    liked_categories = models.ManyToManyField(Movies)
    genreID = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.genre_name


class Reviews(models.Model):
    reviewer = models.CharField(max_length=256)
    reviewID = models.IntegerField(primary_key=True)
    movieID = models.ManyToManyField(Movies)

    def __str__(self):
        return self.reviewer

class Service(models.Model):
    service_name = models.CharField(max_length=256)
    serviceID = models.IntegerField(primary_key=True)
    base_url = models.URLField()
    image_url = models.URLField()

    def __str__(self):
        return self.service_name
