from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('search/',views.search,name="search"),
    path('detail/',views.detail,name="detail"),
    path('blogs/',views.blogs,name="blogs"),
    path('Myprofile/',views.my_profile,name="myprofile"),
    path('<int:id>/profile/',views.profile,name="profile"),
    path('addblog/',views.addblog,name="addblog"),

    path('signin/',views.signin,name="signin"),
    path('signup/',views.signup,name="signup"),
    path('signout/',views.signout,name="signout"),
]