import requests
import json


TMDB_API_KEY ='2ee130f2ba9bf221b6fe5107cffcac46'



def get_movie_genre():
    request_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=en"
    

    genres = requests.get(request_url).json()
    for genre in genres['genres']:


        fields = {
            'name': genre['name'],
        }

        data = {
            "model": "tmdb.genre",
            "pk": genre['id'],
            "fields": fields
        }

        genre_list.append(data)



genre_list = []


get_movie_genre()



file_path = "./genres.json"
with open(file_path, 'w',  encoding='UTF-8') as outfile:
    json.dump(genre_list, outfile, indent="\t", ensure_ascii=False)