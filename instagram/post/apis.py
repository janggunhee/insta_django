from rest_framework import generics, permissions
from rest_framework.response import Response

from member.serializer import UserSerializer
from post.paginations import PostPagination
from post.seriallizers import PostSerializer
from utils.permissions import IsAuthorOrReadOnly
from .models import Post


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        # permissions.IsAuthenticated,
    )
    pagination_class = PostPagination

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


# class PostDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Post.objects.get(pk=pk)
#         except Post.DoesNOtExist:
#             raise
#
#     def get(self, request, pk):
#         Post = self.get_object(pk)
#         serializer = PostSerializer(post, data=request.data)
#         return Response(serializer.data)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        IsAuthorOrReadOnly,

    )

class PostLikeToggle(generics.GenericAPIView):
    queryset = Post.objects.all()
    lookup_url_kwarg = 'post_pk'

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        like_status = False
        #
        if user.like_posts.filter(pk=instance.pk):
            user.like_posts.remove(instance)
        else:
            user.like_posts.add(instance)
            like_status =True
        data = {
            'user': UserSerializer(user).data,
            'post': PostSerializer(instance).data,
            'result': like_status,
        }
        return Response()

