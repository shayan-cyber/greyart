from django.contrib import admin
from blog.models import Post
from blog.models import poem
from blog.models import meme




# Register your models here.
admin.site.register(Post)
admin.site.register(poem)
admin.site.register(meme)
#admin.site.register(BlogComment)


