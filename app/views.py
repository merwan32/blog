from django.shortcuts import render
from .models import Profile,Post

# Create your views here.
def home(request):
    obj= Post.objects.all().order_by('-id')
    head = obj[0]
    posts = obj[1:7]
    return render(request,'home.html',{'posts':posts,'head':head})


def blogs(request):
    posts= Post.objects.all().order_by('-id')
    return render(request,'blogs.html',{'posts':posts})


def search(request):
    search = request.GET['search']
    posts = Post.objects.filter(titre__icontains=search)
    return render(request,'search.html',{'search':search,'posts':posts})

def detail(request):
    return render(request,'detail.html')