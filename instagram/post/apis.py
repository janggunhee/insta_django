from django.http import Http404
from requests import post
from rest_framework import status, mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from post.seriallizers import PostSerializer
from .models import Post


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # def get(self, request, format=None):
    #     posts = Post.objects.all()
    #     serializer = PostSerializer(posts, many=True)
    #     return Response(serializer.data)
    #
    # # def post()구현 (Post 생성)
    # # 중간에 request.user를 사용해야함
    #
    # def post(self, request):
    #     serializer = PostSerializer(data=request.data)
    #     if serializer.is_valid():
    #         # 이 과정에서 author값을 request.user로 채우기
    #         serializer.save(author=self.request.user)
    #         return Response(serializer.data,  status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNOtExist:
            raise

    def get(self, request, pk):
        Post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        return Response(serializer.data)


