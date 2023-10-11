from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
	class Meta:
		ordering = ["id"]
		verbose_name_plural = "Quản lý tài khoản"
	AbstractUser._meta.get_field('email').blank = False
	AbstractUser._meta.get_field('email').null = False
	AbstractUser._meta.get_field('username').blank = False
	AbstractUser._meta.get_field('username').null = False
	AbstractUser._meta.get_field('password').blank = False
	AbstractUser._meta.get_field('password').null = False

class Member(models.Model):
	class Meta:
		ordering = ["id"]
		verbose_name_plural = "Thông tin của tài khoản"
	Date_of_birth = models.CharField('Ngày sinh',max_length=500, null=True, blank=True)
	Address = models.CharField('Địa chỉ',max_length=500, null=True, blank=True)
	Avatar = models.ImageField('Ảnh đại diện',upload_to='user',null=True, blank=True)
	user = models.OneToOneField(User,related_name='user_Member',null=True,blank=True,on_delete=models.CASCADE)

	def __str__(self):	
		return str(self.user)

class Follow(models.Model):
	class Meta:
		ordering = ["id"]
		verbose_name_plural = "Thông tin các tài khoản theo dõi nhau"
	Followed_account = models.ManyToManyField(User,related_name='user_followed',null=True,blank=True)
	user = models.ManyToManyField(User,related_name='user_follow',null=True,blank=True)

	def __str__(self):	
		return str(self.id)

class Post(models.Model):
	class Meta:
		ordering = ["-id"]
		verbose_name_plural = "Bài đăng"
	Content = models.TextField('Nội dung',null=True,blank=True)
	Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
	user = models.ForeignKey(User,related_name='user_post',on_delete=models.CASCADE,null=True,blank=True)
	like = models.ManyToManyField(User,related_name='user_like',null=True,blank=True)
	def __str__(self):	
		return str(self.id)

class Image_Post(models.Model):
	class Meta:
		ordering = ["id"]
		verbose_name_plural = "Ảnh bài đăng"
	Image_post = models.ImageField('Ảnh',upload_to='user',null=True, blank=True)
	post = models.ForeignKey(Post,related_name='post_image',on_delete=models.CASCADE,null=True,blank=True) 
	def __str__(self):	
		return str(self.Image_post)

class Comment(models.Model):
	class Meta:
		ordering = ["id"]
		verbose_name_plural = "Bình luận bài viết"
	body = models.TextField('Nội dung',null=True,blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey(Post, related_name="comments_post" , on_delete=models.CASCADE,null=True,blank=True)
	name = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
