from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('<int:user_id>/', views.get_profile), # get, post
    # path('update/<int:user_id>/', views.userdata_update), # delete, put
    # path('image/<int:user_id>/', views.userdata_profileimage), # post, putpat
    path('<int:user_id>/follow/', views.follow), # post
]   
