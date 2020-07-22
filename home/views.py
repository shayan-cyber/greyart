

# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from blog.models import poem
from blog.models import meme
#from blog.models import PoemComment
#from blog.models import MemeComment

from random import shuffle
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

#html pages
def home(request):
    return  render(request,'home/home.html')
def about(request):
    
    return  render(request,'home/about.html')
def contact(request):
    
    if request.method== 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name,email,phone,content)
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request,"please fill the form properly")
        else:
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,"your message has been successfully sent")



        
    return  render(request,'home/contact.html')  
def Poem(request):
    poems =  poem.objects.all()
    
    my_list=list(poems)
    shuffle(my_list)
    
    params1 ={'poems': my_list}
    return render(request,'home/poemhome.html',params1)
def Meme(request):
    memes =  meme.objects.all()
    my_list=list(memes)
    shuffle(my_list)
    
    params2 ={'meme': my_list}
    return render(request,'home/memehome.html',params2)

    


#html search pages    
def searchblog(request):
    query = request.GET['query']
    
    if len(Post.objects.filter(title__icontains=query))!= 0 or len(Post.objects.filter(content__icontains=query))!= 0 :
        
       
        allpostsTitle = Post.objects.filter(title__icontains=query)
        allpostsContent = Post.objects.filter(content__icontains=query)
        allposts = allpostsTitle.union(allpostsContent)
        params = {'allposts': allposts}
        return render(request,'home/search.html',params)
    else:
        
        return render(request,'home/noresult.html')

      

def searchpoem(request):
    query = request.GET['query']
    if len(poem.objects.filter(title__icontains=query))!= 0 or len(poem.objects.filter(author__icontains=query))!= 0:
        
        
        poemsTitle = poem.objects.filter(title__icontains=query)
        poemsAuthor = poem.objects.filter(author__icontains=query)
        poems = poemsTitle.union(poemsAuthor)
        params1 = {'poems':poems}
        print(poems)
        return render(request,'home/search.html',params1)
    else:
        
        return render(request,'home/noresult.html')
def searchmeme(request):

    query = request.GET['query']        
    if len(meme.objects.filter(title__icontains=query))!=0 or len(meme.objects.filter(author__icontains=query))!=0:
        
        memesTitle = meme.objects.filter(title__icontains=query)
        memesAuthor = meme.objects.filter(author__icontains=query)
        memes = memesTitle.union(memesAuthor)

        params2 = {'memes':memes}
        print(memes)
        return render(request,'home/search.html',params2)
    else:
        
        return render(request,'home/noresult.html')


#authentication APIS        
def handleSignup(request):
    if request.method == 'POST':
        #Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email= request.POST['email']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']

        #checks for errornous input
        if len(username)>15:
            messages.error(request,"username must be under 15 characters")
            return redirect('/')
        # checking if username is alphanumeric or not
        if not username.isalnum():
            messages.error(request,"username should only contain letters and numbers")
            return redirect('/')

        if pass1 != pass2:
            messages.error(request,"PASSWORDS DO NOT MATCH!!")
            return redirect('/')




        #Create the user

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your account has been successfully created")
        return redirect('/')


    else:
        return HttpResponse('404--not found')  

def handleLogin(request):
    if request.method == 'POST':
        #Get the post parameters
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user = authenticate(username=loginusername,password= loginpass)

        if user is not None:
            login(request, user)
            messages.success(request,'successfully logged in')
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials please signup or try again')
            return redirect('/')    
      
    return HttpResponse('404--not found') 

def handleLogout(request):
    logout(request)
    messages.success(request,'successfully logged out')
    return redirect('/')
           
  
def poemPost(request,slug):
    post = poem.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    

    context = {'post': post}
   
    return render(request,'home/poemPost.html',context)
def memePost(request,slug):
    post = meme.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    
    context = {'post': post}
    
   
    return render(request,'home/memePost.html',context)
 #def postComment(request, slug):
    #if request.method=='POST':
       # pass
    #return redirect ("/")    
 #def postComment2(request, slug):
    #if request.method=='POST':
       # pass
   # return redirect ("/")       