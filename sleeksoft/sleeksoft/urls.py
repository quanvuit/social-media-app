"""th URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from Data_Interaction.admin import admin_site
from django.urls import path

from social import views
from rest_framework.routers import DefaultRouter,SimpleRouter
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from django.urls import re_path as url 

from knox import views as knox_views

admin.site.site_header = 'Social Media'                    
admin.site.index_title = 'Site Social Media'                 
admin.site.site_title = 'Social Media site admin' 

router = DefaultRouter()
router.register(r'update-information-user', views.MemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('login', views.login),
    path('keeplogin', views.keep_login),
    url(r'user/auth/', include('knox.urls')),
    path('register',views.create_user),
    path('information-user',views.Information_Member),
    path('follow-user',views.Follow_Member),
    path('list-user-follow',views.List_Follow_Member),
    path('list-user-followed',views.List_Followed_Member),
    path('delete-follow',views.Delete_Follow_Member),
    path('list-user-un-follow',views.List_Un_Follow_Member),
    path('create-post', views.PostViewSet.as_view()),
    path('delete-post', views.Delete_Post),
    path('create-list-image', views.Image_Post_ListViewSet.as_view()),
    path('list-post-user',views.List_Post_user),
    path('list-post',views.List_Post),
    path('search-friend', views.search_friend.as_view()), 
    path('like-post',views.Like_Post),
    path('delete-like-post',views.Remove_Like_Post),
    path('add-comment',views.add_comments),
    path('delete-comment',views.Delete_comments),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
