from .models import *
from .serializers import *
from django.utils import timezone
from rest_framework import status, filters, viewsets, generics
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.auth import AuthToken
from knox.models import AuthToken
from knox.settings import CONSTANTS


@api_view(['POST'])
def login(request):
    try:
        username = request.data['username']
        password = request.data['password']

        if username != None and password != None:
            try:
                serializer = AuthTokenSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                user = serializer.validated_data['user']
                __, token = AuthToken.objects.create(user)

                user.last_login = timezone.now()
                user.save(update_fields=['last_login'])

                message = {
                    'Login information': 'Logged in successfully!',
                    'id': user.id,
                    'email': user.email,
                    'username': user.username,
                    'token': token
                }
                return Response(message, status=status.HTTP_200_OK)
            except:
                message = {
                    'Error': 'Login information is incorrect!'
                }
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            message = {
                'Error': 'Login information cannot be blank!'
            }
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    except:
        message = {
            'Error': 'Login information is incorrect!'
        }
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def keep_login(request):
    try:
        id_user = request.data["id"]
        token = request.data["token"]
        data_user = User.objects.get(id=id_user, is_active=True)
        data_token = AuthToken.objects.get(
            token_key=token[:CONSTANTS.TOKEN_KEY_LENGTH]
        )
        if int(data_token.user_id) == int(data_user.id):
            data_user.last_login = timezone.now()
            data_user.save(update_fields=['last_login'])
            message = {
                'Login information': 'Logged in successfully !',
                'id': data_user.id,
                'email': data_user.email,
                'username': data_user.username,
                'user_Member': MemberSerializer(data_user.user_Member).data,
                'token': token
            }
            return Response(message, status=status.HTTP_200_OK)
        else:
            message = {'Error': 'This account is Invalid !'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    except:
        message = {'Error': 'Invalid data !'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_user(request):
    email = request.data['email']
    dk_email_1 = email.find("@")
    dk_email_2 = email.find(".")

    if dk_email_1 > 0 and dk_email_2 > 0:
        username = request.data['username']
        password = request.data['password']
        confirm_password = request.data['confirm_password']

        data_user_email = User.objects.filter(email=email)
        data_user_email_serializer = UserSerializer(data_user_email, many=True)

        data_user_username = User.objects.filter(username=username)
        data_user_username_serializer = UserSerializer(
            data_user_username, many=True)

        if email != None and username != None and password != None:

            if (email.count(' ') == 0 and
                    username.count(' ') == 0 and
                    password.count(' ') == 0):

                if data_user_username_serializer.data == []:

                    if password == confirm_password:
                        if len(data_user_email_serializer.data) < 2:
                            User.objects.create(email=email,
                                                username=username,
                                                password=password,
                                                is_active=True
                                                )
                            data_user = User.objects.get(email=email,
                                                         username=username,
                                                         is_active=True
                                                         )
                            pw = data_user.password
                            data_user.set_password(pw)
                            data_user.save()

                            Member.objects.create(user=data_user)
                            message = {
                                'Create account ': 'Account successfully created!'
                            }
                            return Response(message, status=status.HTTP_200_OK)
                        else:
                            message = {
                                'Error': 'Your email has a maximum of 2 accounts!'
                            }
                            return Response(message, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        message = {
                            'Error': 'Reconfirm incorrect password!'
                        }
                        return Response(message, status=status.HTTP_400_BAD_REQUEST)
                else:
                    message = {
                        'Error': 'Username already exists!'
                    }
                    return Response(message, status=status.HTTP_400_BAD_REQUEST)
            else:
                message = {
                    'Error': 'Must be a single string of characters!'
                }
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            message = {
                'Error': 'Registration information cannot be left blank!'
            }
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    else:
        message = {
            'Error': 'Invalid email registration!'
        }
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def Information_Member(request):
    username_id = request.query_params.get('username_id')
    data_user = User.objects.get(pk=username_id, is_active=True)
    data_information_user = Member.objects.filter(user=data_user)
    data_information_user_Json = MemberSerializer(
        data_information_user, many=True).data[0]

    message = {
        'Data': data_information_user_Json
    }
    return Response(message, status=status.HTTP_200_OK)


@api_view(['POST'])
def Information_Member_Edit_Avatar(request):
    username_id = request.data['username_id']
    Avatar = request.data['Avatar']
    data_user = User.objects.get(pk=username_id, is_active=True)
    data_information_user = Member.objects.get(user=data_user)
    data_information_user.Avatar = Avatar
    data_information_user.save()

    message = {
        'Update': 'Update Avatar successfully'
    }
    return Response(message, status=status.HTTP_200_OK)


@api_view(['POST'])
def Follow_Member(request):
    username_followed_id = request.data['username_followed_id']
    username_id = request.data['username_id']
    data_user = User.objects.get(pk=username_id, is_active=True)
    data_username_followed = User.objects.get(
        pk=username_followed_id,
        is_active=True
    )
    n = Follow.objects.create()
    n.Followed_account.add(data_username_followed)
    n.user.add(data_user)

    message = {
        'Information_Follow': 'Follow successfully'
    }
    return Response(message, status=status.HTTP_200_OK)


@api_view(['GET'])
def List_Follow_Member(request):
    username_id = request.query_params.get('username_id')
    data_user = User.objects.get(pk=username_id, is_active=True)
    list_data = Follow.objects.filter(user=data_user)
    list_data_Json = FollowSerializer(list_data, many=True).data

    message = {
        'Data': list_data_Json
    }
    return Response(message, status=status.HTTP_200_OK)


@api_view(['GET'])
def List_Followed_Member(request):
    username_id = request.query_params.get('username_id')
    data_user = User.objects.get(pk=username_id, is_active=True)
    list_data = Follow.objects.filter(Followed_account=data_user)
    list_data_Json = FollowSerializer(list_data, many=True).data

    message = {
        'Data': list_data_Json
    }
    return Response(message, status=status.HTTP_200_OK)


@api_view(['GET'])
def Delete_Follow_Member(request):
    follow_id = request.query_params.get('follow_id')
    data_follow = Follow.objects.get(pk=follow_id)
    data_follow.delete()

    message = {
        'Information_Delete': 'Delete Folow_id successfully'
    }
    return Response(message, status=status.HTTP_200_OK)


@api_view(['GET'])
def List_Un_Follow_Member(request):
    username_id = request.query_params.get('username_id')
    data_user = User.objects.get(pk=username_id, is_active=True)
    list_data = Follow.objects.filter(user=data_user)
    list_data_Json = FollowSerializer(list_data, many=True).data

    data_user_all = User.objects.all()
    data_user_all_Json = UserSerializer(data_user_all, many=True).data

    data_user_one = User.objects.get(pk=username_id)
    data_user_one_Json = UserSerializer(data_user_one).data

    data_user_all_Json.pop(0)
    data_user_all_Json.remove(data_user_one_Json)

    for i in list_data_Json:
        for j in data_user_all_Json:
            if int(i['Followed_account'][0]['id']) == int(j['id']):
                data_user_all_Json.remove(j)

    message = {
        'Data': data_user_all_Json
    }
    return Response(message, status=status.HTTP_200_OK)


@api_view(['GET'])
def Delete_Post(request):
    post_id = request.query_params.get('post_id')
    data_post_id = Post.objects.get(pk=post_id)
    data_post_id.delete()

    message = {
        'Information_Delete': 'Delete post_id successfully'
    }
    return Response(message, status=status.HTTP_200_OK)


@api_view(['GET'])
def List_Post_user(request):
    username_id = request.query_params.get('username_id')
    data_user = User.objects.get(pk=username_id, is_active=True)
    list_data = Post.objects.filter(user=data_user)
    list_data_Json = PostSerializer(list_data, many=True).data

    message = {
        'Data': list_data_Json
    }
    return Response(message, status=status.HTTP_200_OK)


@api_view(['GET'])
def List_Post(request):
    username_id = request.query_params.get('username_id')
    data_user = User.objects.get(pk=username_id, is_active=True)

    list_follow = Follow.objects.filter(user=data_user)
    list_follow_Json = FollowSerializer(list_follow, many=True).data

    list_post = Post.objects.all()
    list_post_Json = PostSerializer(list_post, many=True).data

    list_post_home = []
    for i in list_post_Json:
        for j in list_follow_Json:
            if int(i['user']) == int(j['Followed_account'][0]['id']):
                list_post_home.append(i)

    for k in list_post_home:
        k['user'] = UserSerializer(User.objects.get(pk=k['user'])).data

    message = {
        'Data': list_post_home
    }
    return Response(message, status=status.HTTP_200_OK)


@api_view(['GET'])
def Like_Post(request):
    username_id = request.query_params.get('username_id')
    data_user = User.objects.get(pk=username_id, is_active=True)
    post_id = request.query_params.get('post_id')
    data_post = Post.objects.get(pk=post_id)
    data_post.like.add(data_user)

    message = {
        'message': 'successfully'
    }
    return Response(message, status=status.HTTP_200_OK)


@api_view(['GET'])
def Remove_Like_Post(request):
    username_id = request.query_params.get('username_id')
    data_user = User.objects.get(pk=username_id, is_active=True)
    post_id = request.query_params.get('post_id')
    data_post = Post.objects.get(pk=post_id)
    data_post.like.remove(data_user)

    message = {
        'message': 'successfully'
    }
    return Response(message, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_comments(request):
    username_id = request.data['username_id']
    post_id = request.data['post_id']

    data_user = User.objects.get(pk=username_id, is_active=True)
    data_post = Post.objects.get(pk=post_id)
    body = request.data['body']

    Comment.objects.create(name=data_user, post=data_post, body=body)

    message = {'message': 'successfully'}
    return Response(message, status=status.HTTP_200_OK)


@api_view(['GET'])
def Delete_comments(request):
    comment_id = request.query_params.get('comment_id')
    data_comment = Comment.objects.get(pk=comment_id)
    data_comment.delete()

    message = {
        'Information_Delete': 'Delete Comment_id successfully'
    }
    return Response(message, status=status.HTTP_200_OK)


class MemberViewSet(viewsets.ViewSet, generics.UpdateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    parser_classes = [MultiPartParser,]


class Image_Post_ListViewSet(generics.ListCreateAPIView):
    queryset = Image_Post.objects.all()
    serializer_class = Image_PostSerializer
    parser_classes = [MultiPartParser,]


class PostViewSet(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser,]


class search_friend(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']
