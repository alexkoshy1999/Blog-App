from django.shortcuts import render
from django.http import HttpResponse

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
        'post':posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})

   