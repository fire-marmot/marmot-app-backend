# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
# from django.db import models
import requests
# import django
# from django.contrib.auth.models import Movies

STREAMING_SERVICES = [
    'netflix',
    'hulu'
]

STREAMING_SERVICE_CONFIG = {
    'X-RapidAPI-Host':'streaming-availability.p.rapidapi.com',
    'X-RapidAPI-Key':'333634be0fmshfc2408e4e176b0fp10cf59jsn47bf9fc33443'
}


def get_movies_by_service(service):
    STREAMING_API_URL=f'https://streaming-availability.p.rapidapi.com/search/basic?type=movie&genre=18&page=1&output_language=en&language=en&country=us&service={service}'
    r = requests.get(url = STREAMING_API_URL, headers = STREAMING_SERVICE_CONFIG)
    data = r.json()
    final_data = data['results']
    print (final_data[0])
    # print(data)
get_movies_by_service('netflix')
# def get_movie():
#     data = get_movies_by_service('hulu')
#     print(data['imdbID'])
#     # movie = Movies()
#     # for i in data:
#     #     print(i)
#         # movie.movieID = i.imdbID
#         # movie.streaming_service = i.streamingInfo
#         # movie.image_url = i.posterURLs
#         # movie.description = i.overview
#         # movie.genre = i.genres
#     # print(movie)
# get_movie()
