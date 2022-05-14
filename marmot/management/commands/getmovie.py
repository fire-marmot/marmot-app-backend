from django.core.management.base import BaseCommand, CommandError
import requests
from marmot.models import Movies

STREAMING_SERVICES = [
        'netflix',
        'hulu'
    ]

STREAMING_SERVICE_CONFIG = {
        'X-RapidAPI-Host':'streaming-availability.p.rapidapi.com',
        'X-RapidAPI-Key':'333634be0fmshfc2408e4e176b0fp10cf59jsn47bf9fc33443'
    }

class Command(BaseCommand):
        




    def get_movies_by_service(self,service):
        STREAMING_API_URL=f'https://streaming-availability.p.rapidapi.com/search/basic?type=movie&genre=18&page=1&output_language=en&language=en&country=us&service={service}'
        r = requests.get(url = STREAMING_API_URL, headers = STREAMING_SERVICE_CONFIG)
        data = r.json()
        final_data = data['results']
        return final_data[0]
        # print(data)
    # get_movies_by_service('netflix')
    def handle(self, *args, **options):
        data = self.get_movies_by_service('hulu')
        # print(data['imdbID'])
        stream = list(data['streamingInfo'].keys())[0]
        image = list(data['posterURLs'].values())[0]
        movie = Movies()
        movie.title = data['originalTitle']
        movie.movieID = data['imdbID']
        movie.streaming_service = stream
        movie.image_url = image
        movie.description = data['overview']
        movie.genre = data['genres'][0]
        movie.save()

        self.stdout.write(self.style.SUCCESS('Successfully movie "%s"' % movie.title))
# get_movie()