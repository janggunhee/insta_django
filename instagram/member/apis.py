from django.contrib.auth import get_user_model, authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import UserSerializer, SignupSerializer

User = get_user_model()

class Login(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)

        username = request.data['username']
        password = request.data['password']
        user = authenticate(
            username=username,
            password=password,
        )
        if user:
            # 'user'키에 다른 dict로 유저에 대한 모든 정보를 보내줌
            token, token_created = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
                # 'user'키에 해당하는 데이터를 직렬화 해주는 UserSeializer작성 (member/serializer.py)
                'user': UserSerializer(user).data
            }
            return Response(data, status=status.HTTP_200_OK)
        data = {
            'message': 'Invalid credentials'
        }
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)

class Singup(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # 회원가입 후 토큰 생성, 유저정보 및 토큰 키 반환
        # username = request.data['username']
        # password = request.data['password']
        #
        # if User.objects.filter(username=username).exists():
        #     return Response({'message': 'Username already exist'})
        #
        # user = User.objects.create_user(
        #     username=username,
        #     password=password,
        # )
        # token = Token.objects.create(user=user)
        # data = {
        #     'user': UserSerializer(user).data,
        #     'token': token.key,
        # }
        # return Response(data)
