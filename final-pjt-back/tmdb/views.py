# Create your views here.

from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import Genre, Movie, MovieComment
from .serializers import *
from sklearn.feature_extraction.text import CountVectorizer # pip install -U scikit-learn
from sklearn.metrics.pairwise import cosine_similarity
from jellyfish import jaro_winkler_similarity # pip install jellyfish


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET','POST'])
def comment_list(request,movie_pk): #영화 댓글 생성
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieCommentSerializer(data=request.data)
    if request.method == 'POST':  # 생성
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie,user=user)
            comments = movie.TMDBComment.all()
            serializer = MovieCommentSerializer(comments,many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    elif request.method == 'GET':   #조회
        comments_lst = get_list_or_404(MovieComment)
        # comments_lst = movie.TMDBComment.all()   #역참조, 해당 영화에 있는 댓글집합
        serializer = MovieCommentSerializer(comments_lst, many=True)
        return Response(serializer.data)

@api_view(['DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = MovieComment.objects.get(pk=comment_pk)
    if request.method == 'DELETE': #삭제
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # elif request.method == 'PUT':
    #     serializer = MovieCommentSerializer(comment, data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)


# 영화 좋아요 누르기
@api_view(['POST'])
def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user.pk
    if movie.like_users.filter(pk=user).exists():
        movie.like_users.remove(user)
    else:
        movie.like_users.add(user) 
    return Response('movie_like_views.py')

# 영화 봤어요 누르기
@api_view(['POST'])
def movie_seen(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user.pk
    if movie.seen_users.filter(pk=user).exists():
        movie.seen_users.remove(user)
    else:
        movie.seen_users.add(user)
    return Response('movie_seen_views.py')




# 검색 알고리즘 
@api_view(['GET'])
def search_movie(request, movie_name):
    movies = get_list_or_404(Movie)
    serializer = MovieSearchSerializer(movies, many=True)
    serializer = serach(serializer.data, movie_name)
    return Response(serializer[:10])


def serach(lst, keyword):  #lst = 영화정보
    fetch_data = []
    for data in lst :
        if data['poster_path'] :  #영화의 포스터가 있을때,
            tmp = {'pk': 0, 'title': '', 'overview': '' , 'poster_path':'', 'similarity':''} #정보를 담을 폼
            tmp['pk'] = data['pk']; tmp['title'] = data['title']; tmp['overview'] = data['overview']; tmp['poster_path'] = data['poster_path']
            #Jaro-Winkler 유사도는 두 문자열 간의 유사도를 측정하는 데 사용되는 알고리즘. 
            # 이 알고리즘은 문자열의 일치하는 문자 쌍, 문자 순서 및 접두어 접미어를 고려하여 유사도 점수를 계산. 이를 통해 문자열 간의 유사성을 측정할 수 있다. 
            #jaro_winkler_similarity 함수는 두 개의 문자열 인수를 입력으로 받아 Jaro-Winkler 유사도 점수를 반환
            tmp['similarity'] = jaro_winkler_similarity(keyword, data['title']) 
            fetch_data.append(tmp)
    fetch_data.sort(key=lambda x : -x['similarity'])
    return fetch_data



# 추천 알고리즘
# 유저가 좋아할만한 영화
@api_view(['GET'])
def user_like_movie(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    like_movies = user.like_movies.all()
    # print(like_movies)
    # serializer = UserLikeMovieListSerializer(user)  #유저의 pk, username, like_movies이용
    movies = get_list_or_404(Movie)
    movies_serializer = RecommendMovieListSerializer(movies, many=True)  #모든영화의 pk, words, poster_path 이용
    # for test in like_movies:
    #     print(test.pk)
    # 유저의 like_movies
    # user가 좋아요한 영화 key값 담기
    movie_key = [data.pk for data in like_movies] 
    # movie_key = [data['pk'] for data in serializer.data.get('like_movies')] 

    # user가 좋아요 한 영화 index 담기
    idx = []
    for key in movie_key: 
        for i in range(len(movies_serializer.data)): #전체 영화의 pk, words, poster_path 탐색 
            #영화랑 키가 일치한다면,
            if key == movies_serializer.data[i]['pk'] and movies_serializer.data[i]['poster_path'] != None:
                idx.append(i)
                break

    # 모든영화들의 words 담기
    movie_words = [data.get('words') for data in movies_serializer.data]
    # 유사 영화 pk 반환
    result = recommend_movies_names(movie_words, idx, movies_serializer, user_pk)
    print(result)
    # 유사 영화들의 데이터 담기
    final_movie = [get_object_or_404(Movie, pk=i) for i in result]
    final_serializer = UserChoiceSimilarMovieSerializer(final_movie, many=True)
    return Response(final_serializer.data)

def recommend_movies_names(movie_words, idx, movies, user_pk):
    # 텍스트 데이터를 특성 벡터로 변환하는 데 사용
    user = get_object_or_404(User, pk=user_pk)
    countVec = CountVectorizer(max_features=10000, stop_words='english')

    # 영화 키워드 벡터라이징
    dataVectors = countVec.fit_transform(movie_words).toarray()

    # 코사인 유사도
    similarity = cosine_similarity(dataVectors)

    # 유사도 내림차순 영화의 인덱스
    idx_collection = []
    for i in idx:
        distances = similarity[i] #유사도 정보를 distance에 각각할당
        #enumerate를 사용해 (인덱스, 값)의 형태 => 내림차순으로 정렬
        listofMovies = sorted(list(enumerate(distances)), key=lambda x:x[1], reverse=True)[:10]
        # print('인덱스를 pk로')
        # print(listofMovies)
        # print('확인')
        idx_collection.extend(listofMovies)
    # idx_collection.sort(key=lambda x: x[1], reverse=True)[:10]

    result_collection=[]
    for movie_idx, one_collection in idx_collection:
        # print(movies.data[movie_idx].get('pk'))
        target_movie = get_object_or_404(Movie, pk=movies.data[movie_idx].get('pk'))

        for genre in target_movie.genres.all():

            if user.like_genre == genre.name:
                one_collection *=1.1
                break   

        result_collection.append((movie_idx,one_collection))
    result_collection =  sorted(result_collection, key=lambda x: x[1], reverse=True)[:10]

    
        # if user.like_genre in target_movie:
        #     one_collection *= 1.1
    
    # 인덱스를 pk로 바꾸기
    pk_collection = []
    for idx in result_collection:
        if movies.data[idx[0]]['poster_path'] != None :
            pk_collection.append(movies.data[idx[0]]['pk'])
    # print(pk_collection)
    return pk_collection












# @api_view(['GET', 'POST'])
# # @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def rating_list_create(request, movie_id):
#     movie = get_object_or_404(Movie, id=movie_id)
#     if request.method=='GET':
#         ratings = movie.ratings.all()
#         serializer= RatingSerializer(ratings, many=True)
#         return Response(serializer.data)
#     else:
#         serializer = RatingSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(user=request.user, movie=movie)
#             return Response(serializer.data)

# @api_view(['DELETE'])
# # @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def rating_delete(request, rating_pk):
#     rating = get_object_or_404(Rating, pk=rating_pk)
#     rating.delete()
#     return Response({'id': rating_pk})

# @api_view(['PUT'])
# # @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def rating_update(request,movie_pk):
#     movie = get_object_or_404(Movie, id=movie_pk)
#     rating = get_object_or_404(Rating, user=request.user)
#     rating.delete()
#     serializer = RatingSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(user=request.user, movie=movie)
#         return Response(serializer.data)