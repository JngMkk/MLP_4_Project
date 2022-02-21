from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def community(request):
    return render(request, 'community.html')

def index_di(request):
    return HttpResponse("안녕하세요 pybo에 오신 것을 환영합니다.")