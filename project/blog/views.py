from django.shortcuts import render
from .models import Post

# Create your views here.
posts = [
    {
        'author': 'Alex',
        'title': 'Blog Post',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Django',
        'title': 'Blog Post2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]
def home(request):
    context={
        'post': Post.objects.all()
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})

   