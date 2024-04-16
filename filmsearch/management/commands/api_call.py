from django.core.management.base import BaseCommand

from filmsearch.APIConnection import retrieve_movies, retrieve_genres
from filmsearch.models import Films, Genre


class Command(BaseCommand):
    help = "Accesses API and returns movies"

    def add_arguments(self, parser):
        parser.add_argument("firstpage", nargs="+", type=int, default=1)
        parser.add_argument("lastpage", nargs="+", type=int, default=1)

    def handle(self, *args, **options):
        print(options)
        api_films = retrieve_movies(options["firstpage"][0], options["lastpage"][0])  # This should return a list of dictionaries

        # You might want to clear the Films table before repopulating it
        # Be cautious with this as it will delete all existing entries in the Films table
        # Films.objects.all().delete()

        genres = retrieve_genres()
        for genre_data in genres:
            Genre.objects.get_or_create(
                api_genre_id = genre_data['id'],
                defaults = {
                    'genre_name': genre_data['name']}
            )

        # Create Films objects only if they don't already exist
        for film_data in api_films:
            poster_url = "https://image.tmdb.org/t/p/w500" + film_data['poster_path']
            print("poster_path:", film_data['poster_path'])  # This will print the poster_path from the API
            print("Poster URL:", poster_url)  # This will print the full URL

            Films.objects.get_or_create(
                name=film_data['original_title'],
                defaults={
                    'description': film_data['overview'],
                    'poster_image': poster_url,
                    'lang': film_data['original_language'],
                    'rating': film_data['vote_average'],
                    'release_date': film_data['release_date'],
                    'genres': film_data['genre_ids']
                }
            )