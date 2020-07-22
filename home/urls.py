from django.contrib import admin
from django.urls import path
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.home, name='home'),
    
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('searchblog/',views.searchblog,name='search1'),
    path('searchpoem/',views.searchpoem,name='search2'),
    path('searchmeme/',views.searchmeme,name='search3'),
    path('poem/',views.Poem,name='poem'),
    path('meme/',views.Meme,name='meme'),
    path('signup/',views.handleSignup,name='handleSignup'),
    path('login/',views.handleLogin,name='handleLogin'),
    path('logout/',views.handleLogout,name='handleLogout'),
    path('poem/<str:slug>',views.poemPost,name='poemPost'),
    path('meme/<str:slug>',views.memePost,name='memePost'),
    #path('postComment/' , views.postComment, name="postComment"),
    #path('postComment2/' , views.postComment2, name="postComment2")


    
   
]