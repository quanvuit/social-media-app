from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model=User
		fields=('id','username','email','password','user_Member')
		extra_kwargs = {'password': {'write_only': True}}

class FollowSerializer(serializers.ModelSerializer):
	Followed_account = UserSerializer(many=True,read_only=True)
	user = UserSerializer(many=True,read_only=True)

	class Meta:
		model=Follow
		fields='__all__'

class MemberSerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)

	class Meta:
		model=Member
		fields='__all__'

class UserSerializer(serializers.ModelSerializer):
	user_Member = MemberSerializer()
	user_followed = FollowSerializer(many=True,read_only=True)

	class Meta:
		model=User
		fields=('id','username','email','password','user_Member','user_followed')
		extra_kwargs = {'password': {'write_only': True}}

class FollowSerializer(serializers.ModelSerializer):
	Followed_account = UserSerializer(many=True,read_only=True)
	user = UserSerializer(many=True,read_only=True)

	class Meta:
		model=Follow
		fields='__all__'

class CommentSerializer(serializers.ModelSerializer):
	name = UserSerializer(read_only=True)

	class Meta:
		model=Comment
		fields='__all__'

class Image_PostSerializer(serializers.ModelSerializer):

	class Meta:
		model=Image_Post
		fields='__all__'

class PostSerializer(serializers.ModelSerializer):
	post_image = Image_PostSerializer(many=True,read_only=True)
	uploaded_images = serializers.ListField(
		child = serializers.ImageField(
			max_length = 1000000,
			allow_empty_file = False,
			use_url = False),
			write_only=True
		)
	like = UserSerializer(many=True,read_only=True)
	comments_post = CommentSerializer(many=True,read_only=True)

	class Meta:
		model=Post
		fields='__all__'

	def create(self,validated_data):
		uploaded_images = validated_data.pop("uploaded_images")
		post = Post.objects.create(**validated_data)
		for image in uploaded_images:
			Image_Post.objects.create(post=post, Image_post=image)
		return validated_data


