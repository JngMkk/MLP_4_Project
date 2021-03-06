"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('community/', views.community, name='community'),
    #상동
    path('pybo/', include('pybo.urls')),
    path('login/', views.login, name='login'),
    path('signin/', views.signin, name='signin'),
    # path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('pybo1/', include('pybo1.urls')),
    path('front_data/', views.front_data, name='front_data'),
    path('gangwon/', views.gangwon, name='gangwon'),
    path('example/', views.example, name='example'),
    path('geumgang/', views.geumgang, name='geumgang'),
    path('daeduk/', views.daeduk, name='daeduk'),
    path('duwon/', views.duwon, name='duwon'),
    path('youngnam/', views.youngnam, name='youngnam'),
    path('jeju/', views.jeju, name='jeju'),
]


