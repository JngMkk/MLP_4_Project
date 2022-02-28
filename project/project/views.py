from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate


from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def community(request):
    return render(request, 'community.html')

def index_di(request):
    return HttpResponse("안녕하세요 pybo에 오신 것을 환영합니다.")

# def login(request):
#     return render(request, "/accounts/templates/login.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

# 안쓰는 코드(signin은) , signup으로 대체함
def signin(request):
    return render(request, "signin.html")


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'signup.html', backend='django.contrib.auth.backends.ModelBackend')
    return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def front_data(request):
    return render(request, 'front_data.html')

def example(request):
    return render(request, 'example.html')

def gangwon(request):
    return render(request, 'gangwon.html')

def geumgang(request):
    return render(request, 'geumgang.html')

def daeduk(request):
    return render(request, 'daeduk.html')

def duwon(request):
    return render(request, 'duwon.html')

def youngnam(request):
    return render(request, 'youngnam.html')

def jeju(request):
    return render(request, 'jeju.html')