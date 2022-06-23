
from core.views import Home, ProfileList, ProfileCreate,Watch,ShowMovieDetail,ShowMovie
from django.urls import path
app_name='core'
 
urlpatterns = [    
    path('',Home.as_view()),
    path('profile/',ProfileList.as_view(),name='profile_list'),# 프로필 리스트
    path('profile/create/',ProfileCreate.as_view(),name='profile_create'),# 프로필 생성
    path('watch/<str:profile_id>/',Watch.as_view(),name='watch'), # watch 
    path('movie/detail/<str:movie_id>/',ShowMovieDetail.as_view(),name='show_det'), #영화 상세 정보
    path('movie/play/<str:movie_id>/',ShowMovie.as_view(), name='play') # 영화 시청 

]