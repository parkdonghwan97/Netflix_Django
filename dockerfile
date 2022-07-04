#./Dockerfile
FROM python:3.8.6
# 기반이 될 이미지

# 작업 디렉터리(디폴트) 설정
WORKDIR /usr/src/app

# Install Pacakges
# 현재 패키지 정보를 도커파일에 복사
## Install packages
COPY requirements.txt ./
RUN pip install -r requirements.txt

## Copy all src files
COPY . .
## Run the application on the port 8080  
EXPOSE 8000
# gunicorn 배포 명령어
# CMD ["gunicorn", "--bind", "허용하는 IP:열어줄 포트", "project.wsgi:application"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "django_netflix.wsgi:application"]
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]