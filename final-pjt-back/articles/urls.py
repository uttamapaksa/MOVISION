# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    #리뷰게시판
    path('reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('reviews/<int:review_pk>/create', views.review_comment_create),  # 리뷰게시판 댓글 생성
    path('review_comments/', views.review_comment_list),
    path('review_comments/<int:review_comment_pk>/', views.review_comment_detail),
    # path('reviews/<int:review_pk>/comments/', views.review_comment_create),
    #파티게시판
    path('parties/', views.party_list),
    path('parties/<int:party_pk>/', views.party_detail),
    path('party_comments/', views.party_comment_list),
    path('party_comments/<int:party_comment_pk>/', views.party_comment_detail),
    path('parties/<int:party_pk>/comments/', views.party_comment_create),

    # # 필수 작성
    # path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # optional UI
    # path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
