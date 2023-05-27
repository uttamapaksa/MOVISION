import requests
import json

import json
with open ("moviesemple.json", "r",  encoding='UTF-8') as f:
    data = json.load(f)



TMDB_API_KEY ='2ee130f2ba9bf221b6fe5107cffcac46'



def get_word_datas():
    for i in range(1, 110):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=en-US&page={i}"

        movies = requests.get(request_url).json()

        for movie in movies['results']:  #영화 각각의 정보
            
            #해당영화의 배우정보 요청

            response = f"https://api.themoviedb.org/3/movie/{movie['id']}/credits?api_key={TMDB_API_KEY}"
            cnt = 0
            actors = []
            movies = requests.get(response).json()
            for person in movies['cast']:
                
                cnt +=1
                if person.get('known_for_department') != 'Acting': continue  #배우정보만 
                if cnt ==5: break  # 전체 배우 받아올땐 주석처리
                actors.append(person['id'])

                pk_actor_list.append(person['id'])
                make_actor_list.append([person['name'],person['profile_path']])


            #해당영화의 유튜브 키 요청

            response = f"https://api.themoviedb.org/3/movie/{movie['id']}/videos?api_key={TMDB_API_KEY}"
            result_youtube = ''
            youtube = requests.get(response).json()
            for youtube1 in youtube['results']:
                if youtube1['site'] == 'YouTube':
                    result_youtube+=youtube1['key']
                    break

            if movie.get('release_date', ''):
                fields = {
                    'words': movie['overview'],    
                }

                thisdata = {
                    "pk": movie['id'],
                    "model": "tmdb.movie",
                    "fields": fields
                }
                fields2 = {    
                    'actors' : actors
                }

                thisdata2 = {
                    "pk": movie['id'],
                    "model": "tmdb.movie",
                    "fields": fields2
                }
                fields3 = {    
                    'youtube_key' : result_youtube
                }

                thisdata3 = {
                    "pk": movie['id'],
                    "model": "tmdb.movie",
                    "fields": fields3
                }

                word_list.append(thisdata)
                actor_list.append(thisdata2)
                youtube_list.append(thisdata3)

def get_movie_actor():
    for i in range(len(make_actor_list)):
        fields = {
            'name': make_actor_list[i][0],
            'poster_path': make_actor_list[i][1],
        }

        data3 = {
            "model": "tmdb.actor",
            "pk": pk_actor_list[i],
            "fields": fields
        }
        result_actor.append(data3)

word_list = []
youtube_list = []
actor_list = []
make_actor_list = []
pk_actor_list = []
result_actor = []
get_word_datas()
get_movie_actor()
for i in range(len(data)):
    data[i]['fields']['words'] = word_list[i]['fields']['words']
    data[i]['fields']['actors'] = actor_list[i]['fields']['actors']
    data[i]['fields']['youtube_key'] = youtube_list[i]['fields']['youtube_key']



file_path = "./movies.json"
with open(file_path, 'w',  encoding='UTF-8') as outfile:
    json.dump(data, outfile, indent="\t", ensure_ascii=False)


# 배우json 생성

file_path = "./actors.json"
with open(file_path, 'w',  encoding='UTF-8') as outfile:
    json.dump(result_actor, outfile, indent="\t", ensure_ascii=False)