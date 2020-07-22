from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post
from django.contrib import messages


# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all().order_by('-timeStamp')
    
    context = {'allPosts':allPosts}
    
    return render(request,'blog/bloghome.html',context)
def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    
    
    context = {'post': post}
   
    return render(request,'blog/blogPost.html',context)
#def postComment(request):
    #if request.method=='POST':
         
        # comment = request.POST.get('comment')
        # user = request.user
         #postSno = request.POST.get('postSno')
        # post = Posts.objects.get(sno=postSno)
        #parent = 
         #comment = BlogComment(comment=comment , user=user,post=post)
         #comment.save()
         #messages.success(request,"your comment has been posted")
    #return redirect ("/blog/{post.slug}")   