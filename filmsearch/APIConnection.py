import requests

def connect(firstpage, lastpage):
    print("connected")
    output = list()

    for page in range(firstpage, lastpage + 1):
        url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page={page}&sort_by=popularity.desc"
        api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NWI4ZDFkNTVhZmRjYWUwOGVjMDQ4ZWVlNjRmZDU3ZCIsInN1YiI6IjY2MGViODYzZTE4ZTNmMDE0YWEzMmYyZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.oNwVMAnLjuU9ptyWKIVqqPJiUor6KFn61wU09Dxy1CI"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        response = requests.get(url, headers=headers)
        data = response.json()

        output.extend(data['results'])
    
    return output

