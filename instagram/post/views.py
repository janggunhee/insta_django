from django.shortcuts import render

from .models import Post


def post_list(request):
    """
    모든 Post목록을 리턴
    template 'post/post_list.html'을 사용    :param request:
    :return:
    """

    posts = Post.objects.all()
    context = {
        'posts':'post',
    }
    return render(request, 'blog/post_list.html', context)


