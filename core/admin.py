from django.contrib import admin

from .models import Movie,Profile,CustomUser,Video  

admin.site.register(Movie) #관리자 추가를 위한 레지스터
admin.site.register(Profile)
admin.site.register(CustomUser)
admin.site.register(Video)
  # admin에 모듈 추가
