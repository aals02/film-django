import requests

def connect():
    print("connected")
    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
    api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NWI4ZDFkNTVhZmRjYWUwOGVjMDQ4ZWVlNjRmZDU3ZCIsInN1YiI6IjY2MGViODYzZTE4ZTNmMDE0YWEzMmYyZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.oNwVMAnLjuU9ptyWKIVqqPJiUor6KFn61wU09Dxy1CI"
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)
    return response.json()['results']


