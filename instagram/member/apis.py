import token

from rest_framework import status
from rest_framework.authtoken.models import Token

from rest_framework.compat import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView

from member.serializer import UserSerializer


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

        else:
            data = {
                'message': 'Invalid credentials'
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
