from django.shortcuts import render,redirect
from .models import Profile,Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q

# Create your views here.
def home(request):
    obj= Post.objects.all().order_by('-id')
    head = obj[0]
    posts = obj[1:7]
    return render(request,'home.html',{'posts':posts,'head':head})


def blogs(request):
    posts= Post.objects.all().order_by('-id')
    return render(request,'blogs.html',{'posts':posts})

def addblog(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        post = request.FILES['image']
        type = request.POST['type']
        titre = request.POST['titre']
        text = request.POST['text']
        posts = Post.objects.create(profile=profile,image=post,type=type,titre=titre,text=text)
        return redirect('myprofile')
    return render(request,'addblog.html')

def my_profile(request):
    posts= Post.objects.filter(profile__user=request.user).order_by('-id')
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        profile.profile_picture = request.FILES['img']
        profile.save()
    return render(request,'myprofile.html',{'posts':posts,'profile':profile})

def profile(request,id):
    posts= Post.objects.filter(profile__id=id).order_by('-id')
    profile = Profile.objects.get(id=id)
    return render(request,'profile.html',{'posts':posts,'profile':profile})


def search(request):
    search = request.GET['search']
    posts = Post.objects.filter(Q(titre__icontains=search)| Q(type__icontains=search))
    return render(request,'search.html',{'search':search,'posts':posts})

def detail(request,id):
    post = Post.objects.get(id=id)
    return render(request,'detail.html',{'post':post})

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = User.objects.get(email=email.lower()).username
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect("home")
    return render(request,'auth/signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email'].lower()
        work = request.POST['work']
        password = request.POST['password']
        cpassword = request.POST['repassword']
        if password == cpassword :
            user = User.objects.create_user(username=username,email=email,password=password)
            profil = Profile.objects.create(user=user,work=work)
            if profil :
                user = authenticate(username=username,password=password)
                login(request,user)
                return redirect("home")
    return render(request,'auth/signup.html')

def signout(request):
    logout(request)
    return redirect('home')