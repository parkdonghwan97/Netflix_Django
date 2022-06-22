
from django.urls import path
from .views import Home, ProfileList ,ProfileCreate,Watch
app_name='core'
 
urlpatterns = [    
    path('',Home.as_view()),
    path('profile/',ProfileList.as_view(),name='profile_list') ,# 프로필 리스트
    path('profile/create/',ProfileCreate.as_view(),name='profile_create') ,# 프로필 생성
    path('watch/<str:profile_id>/',Watch.as_view(),name='watch'), # watch 


]