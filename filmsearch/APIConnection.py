import requests

def retrieve_movies(firstpage, lastpage):
    print("connected")
    output = list()

    api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NWI4ZDFkNTVhZmRjYWUwOGVjMDQ4ZWVlNjRmZDU3ZCIsInN1YiI6IjY2MGViODYzZTE4ZTNmMDE0YWEzMmYyZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.oNwVMAnLjuU9ptyWKIVqqPJiUor6KFn61wU09Dxy1CI"

    for page in range(firstpage, lastpage + 1):
        url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page={page}&sort_by=popularity.desc"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        response = requests.get(url, headers=headers)
        data = response.json()

        output.extend(data['results'])
    
    return output

def retrieve_genres():
    api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NWI4ZDFkNTVhZmRjYWUwOGVjMDQ4ZWVlNjRmZDU3ZCIsInN1YiI6IjY2MGViODYzZTE4ZTNmMDE0YWEzMmYyZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.oNwVMAnLjuU9ptyWKIVqqPJiUor6KFn61wU09Dxy1CI"
    output = list()
    url = "https://api.themoviedb.org/3/genre/movie/list?language=en"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # This will raise an exception for HTTP errors
        data = response.json()
        return data.get('genres', [])  # Returns an empty list if 'genres' key is missing
    except requests.RequestException as e:
        print(f"Failed to retrieve genres: {e}")
        return []
