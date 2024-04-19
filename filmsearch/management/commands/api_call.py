from django.core.management.base import BaseCommand
from filmsearch.APIConnection import retrieve_movies, retrieve_genres
from filmsearch.models import Films, Genre


class Command(BaseCommand):
    help = "Accesses API and returns movies"

    def add_arguments(self, parser):
        parser.add_argument("firstpage", nargs="+", type=int, default=1)
        parser.add_argument("lastpage", nargs="+", type=int, default=1)

    def handle(self, *args, **options):
        api_films = retrieve_movies(options["firstpage"][0], options["lastpage"][0])  # This should return a list of dictionaries

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

            film, created = Films.objects.get_or_create(
                name=film_data['original_title'],
                defaults={
                    'description': film_data['overview'],
                    'poster_image': poster_url,
                    'lang': film_data['original_language'],
                    'rating': film_data['vote_average'],
                    'release_date': film_data['release_date']
                }
            )

            # Retrieve or create genre instances and add them to the film
            genre_ids = film_data['genre_ids']
            g_list = list()
            for gid in genre_ids:
                genre_name = Genre.objects.get_or_create(api_genre_id=gid)[0]
                g_list.append(genre_name)

            film.genres.set(g_list)
        print("API call successful")