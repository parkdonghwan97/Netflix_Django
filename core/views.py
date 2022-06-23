from django.shortcuts import redirect, render
from django.views import View             #클래스 기반 접근 방식 사용.  
from django.contrib.auth.decorators import login_required # 로그인한 사용자만 열 수 있도록 함
from django.utils.decorators import method_decorator
from core.models import Movie, Profile # 디스패치를 장식하기 위해 생성된 메서드 사용 
from .forms import ProfileForm # 프로필 양식

class Home(View):
    def get(self,request,*args,**kwargs):
        # 홈 보기 사용자가 이미 로그인한 경우 해당 사용자 인덱스 페이지를 보지 않고 홈페이지에 엑세스할 때 프로필 페이지로 보냄 
        if request.user.is_authenticated:  # 홈페이지 요청시 사용자 인증 후 리다이렉션
            return redirect('core:profile_list')
        return render(request,'index.html') # 정적파일에서 템플릿 폴더를 확인, 복제 시작, 파일을 보게된다. url.py파일에 추가 

@method_decorator(login_required,name='dispatch')   # 디스패치 시트 -> 서비스는 보기에 대한 경로제공 해야함. core.urls.py파일에서 프로필 목록 가져옴
class ProfileList(View):
    def get(self,request,*args,**kwargs):  #    프로필을 얻음
        profiles=request.user.profiles.all()    
        return render(request, 'profileList.html',
                {'profiles':profiles}               # 프로필 목록 제공할 보기
                                                    # 로그인하지 않은 사람이 이 정보를 보려고 하면 오류 
                                                    # 익명의 사용자 인스턴스는 프로필 인스턴스에 이 프로필 인스턴스가 없거나 프로필 사진 게시하지 않음
                                                    # 경로를 보호해야함. -> 로그인한 사용자만 열 수 있도록
)


# 누군가가 프로필을 만든 장소에 가기 전에 그 사람이 로그인 해야함 -> Profile_List에서 했던 작업 그대로 (데코레이터)
@method_decorator(login_required,name='dispatch')  
#프로필(등급)  생성 클래스 
class ProfileCreate(View):
    def get(self,request, *args, **kwargs):    # 프로필 생성 추가 의견 양식을 남겨  요청을 랜더링하고 프로필 유지, HTML생성
        form=ProfileForm()  # 프로필 양식 인스턴스 생성 , 기능은 POST메서드 내부에 있을 것
        return render(request,'profileCreate.html',{
            'form':form
        })

    # POST메서드 관련 요쳥과 행동 
    def post(self,request,*args, **kwargs):
        form=ProfileForm(request.POST or None) # 포스트 요청을 받거나 안받거나

        # 내부에 아무것도 없으면 제대로 수행되야함. 양식이 유효한지 확인
        if form.is_valid():
            print(form.cleaned_data)
            profile = Profile.objects.create(**form.cleaned_data) #profile변수에 생성된 데이터 저장 ( 프로필에 대한 로그인 선택을 위함)
            if profile:
                request.user.profiles.add(profile)
                return redirect('core:profile_list')
        return render(request,'profileCreate.html',
        {
            'form':form
        })
@method_decorator(login_required,name='dispatch')  
class Watch(View):
    def get(self,request,profile_id,*args, **kwargs):
        try:
            profile=Profile.objects.get(uuid=profile_id)  # 프로필을 받고 
            movies=Movie.objects.filter(age_limit=profile.age_limit)# DB에서 모든 영화수집 - 나이별 제한을 두어 필터링

            try:
                showcase=movies[0]
            except :
                showcase=None

            if profile not in request.user.profiles.all():#프로필 있는 지 확인 후 리다이렉트
                return redirect(to='core:profile_list')  # 프로필 없는 경우 프로필 리스트로 리다이렉트
            
            #print("============"*1000)
            # print(profile)
            # print("@@@",movies)
            # print("@@@@",showcase)
            return render(request,'movieList.html',{
            'movies':movies,
            'show_case':showcase,
            })
            # 프로필 있으면  준비된 영화목록  반환
        except Profile.DoesNotExist:  # 오류 or  프로필 확인 불가한 경우 예외 처리
            return redirect(to='core:profile_list')
             

@method_decorator(login_required,name='dispatch')  
class ShowMovieDetail(View):
    def get(self,request,movie_id,*args, **kwargs):
        try: # 영화 id로 확인 
            movie=Movie.objects.get(uuid=movie_id)
            return render(request,'movieDetail.html',{
                'movie':movie,
            })
        except Movie.DoesNotExist:
            return redirect('core:profile_list')

@method_decorator(login_required,name='dispatch') 
class ShowMovie(View): # 영화 보여주는 클래스       쿼리목록으로 만들어 list(movie)
    def get(self,request,movie_id,*args, **kwargs):
        try:
            movie=Movie.objects.get(uuid=movie_id)
            movie=movie.videos.values()
            
            return render(request,'showMovie.html',{
                'movie':list(movie)
            })
        except Movie.DoesNotExist:
            return redirect('core:profile_list')