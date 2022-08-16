from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('search/',views.search,name="search"),
    path('detail/',views.detail,name="detail"),
    path('blogs/',views.blogs,name="blogs"),
]