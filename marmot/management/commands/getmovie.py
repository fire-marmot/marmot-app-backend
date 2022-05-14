from django.core.management.base import BaseCommand, CommandError
import requests
from marmot.models import Movies

STREAMING_SERVICES = [
        'netflix',
        'hulu',
        'prime',
        'disney',
        'hbo',
        'paramount',
        'apple'
        
    ]

STREAMING_SERVICE_CONFIG = {
        'X-RapidAPI-Host':'streaming-availability.p.rapidapi.com',
        'X-RapidAPI-Key':'333634be0fmshfc2408e4e176b0fp10cf59jsn47bf9fc33443'
    }

class Command(BaseCommand):
        
    # def add_arguments(self, parser):
    #     parser.add_argument('--str', type=str)

    def get_movies_by_service(self,service):
        STREAMING_API_URL=f'https://streaming-availability.p.rapidapi.com/search/basic?type=movie&page=1&output_language=en&language=en&country=us&service={service}'
        r = requests.get(url = STREAMING_API_URL, headers = STREAMING_SERVICE_CONFIG)
        data = r.json()
        final_data = data['results']
        return final_data
        # print(data)
    # get_movies_by_service('netflix')
    def handle(self,*args, **options):
        service = 'apple'
        data = self.get_movies_by_service(service)
        # print(data['imdbID'])
        # url = list(data['streamingInfo'][service][0].values())
        for i in data:
            # stream = i['streamingInfo']
            stream = list(i['streamingInfo'].keys())[0]
            image = list(i['posterURLs'].values())[0]
            url = i['streamingInfo'][service]['us']['link']
            movie = Movies()
            movie.title = i['originalTitle']
            movie.movieID = i['imdbID']
            movie.streaming_service = stream
            movie.streaming_url = url
            movie.image_url = image
            movie.description = i['overview']
            movie.genre = i['genres'][0]
            movie.average_rating = i['imdbRating']
            movie.save()

        self.stdout.write(self.style.SUCCESS('Successfully movie'))
# get_movie()