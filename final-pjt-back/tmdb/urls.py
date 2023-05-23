from django.urls import path
from . import views

app_name="tmdb"

urlpatterns = [
    path('', views.movie_list),
    path('detail/<int:movie_pk>/', views.movie_detail),
    path('detail/<int:movie_pk>/comment_list/', views.comment_list), # 생성, 조회
    path('detail/<int:movie_pk>/like/', views.movie_like), # 좋아요
    path('detail/<int:movie_pk>/seen/', views.movie_seen), # 봤어요
    path('movie_comment/<int:comment_pk>/', views.comment_detail), # 삭제 , 수정 , 세부페이지는 생략
    # path('detail/<int:rating_pk>/rating_delete/', views.rating_delete),
    # path('detail/<int:movie_pk>/rating_update/', views.rating_update),
]