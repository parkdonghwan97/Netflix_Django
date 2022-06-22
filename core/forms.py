from django.forms import ModelForm
from .models import Profile

# 프로필 클래스 생성 폼
class ProfileForm(ModelForm):
    # 
    class Meta:
        model=Profile  
        exclude=['uuid'] # uuid는 백엔드에서 동적으로 생성되는 필드