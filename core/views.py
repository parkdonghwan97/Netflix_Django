from django.shortcuts import render
from django.views import View               #클래스 기반 접근 방식 사용.  

class Home(View):
    def get(self,request,*args,**kwargs):
        return render(request,'index.html') # 정적파일에서 템플릿 폴더를 확인, 복제 시작, 파일을 보게된다. url.py파일에 추가 
