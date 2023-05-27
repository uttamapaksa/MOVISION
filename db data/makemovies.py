import requests
import json


TMDB_API_KEY ='2ee130f2ba9bf221b6fe5107cffcac46'



def get_movie_datas():
    for i in range(1, 110):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        
        movies = requests.get(request_url).json()
        for movie in movies['results']:
            if movie.get('adult') : continue
            if not movie.get('poster_path') : continue
            if not movie.get('backdrop_path') : continue
            if movie.get('vote_average') == 10 : continue
            if movie.get('release_date', ''):
                fields = {
                    'title': movie['title'],
                    'release_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_count': movie['vote_count'],
                    'vote_average': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'backdrop_path': movie['backdrop_path'],
                    'youtube_key' : '',
                    'genres': movie['genre_ids'],
                    'actors' : [],
                    'words': [],
                }

                data = {
                    "model": "tmdb.movie",
                    "pk": movie['id'],
                    "fields": fields
                }

                movie_list.append(data)



movie_list = []


get_movie_datas()



file_path = "./moviesemple.json"
with open(file_path, 'w',  encoding='UTF-8') as outfile:
    json.dump(movie_list, outfile, indent="\t", ensure_ascii=False)