from pydoc import describe
from pyexpat import model
from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser  
import uuid 


AGE_CHOICES =(
    ('ALL','ALL'),   # 하나는 DB저장용 하나는 사용자에게 표시용
    ('Students','Students'),
    ('Kids','Kids')
)
MOVIE_TYPE=(
    ('Seasonal','Seasonal'),
    ('Single','Single'),
    ('Test_ADD','Test_ADD')

)



# 사용자 정의 클래스       
class CustomUser(AbstractUser):
    # 추가하려는 프로필 필드에 모든 권한 부여
    profiles = models.ManyToManyField('Profile',  blank=True)

# 사용자 프로필 클래스
class Profile(models.Model):
    name = models.CharField(max_length=225)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)
    #프로필에 대한 uuid   #특정모듈 요청 or 구별
    uuid = models.UUIDField(default=uuid.uuid4,unique=True) # 기본값 4 
    
    

# 영화 클래스
class Movie(models.Model):
    title = models.CharField(max_length=225)
    description=models.TextField(blank=True,null=True) # 영화 설명
    created = models.DateTimeField(auto_now_add=True) # 날짜 추가 
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(max_length=10,choices=MOVIE_TYPE ) # 영화 타입, 시즌영화인지 단일 영화인지 
    videos = models.ManyToManyField('Video') # 비디오 관련 
    flyer = models.ImageField(upload_to='flyers',blank=True,null=True)# 포스터 or 전단지(?) 이미지
    age_limit = models.CharField(max_length=10,choices=AGE_CHOICES,blank=True,null=True)

# 개별 비디오나 영화 파일을 유지하려는 비디오 모델(?)
class Video(models.Model):
    # seasonal movie인 경우   ep1  , ep2 , ep3 ----
    tiltle=models.CharField(max_length=225,blank=True,null=True)
    file =models.FileField(upload_to='movies')# 비디오 파일