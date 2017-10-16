from django.http import HttpResponse
from django.shortcuts import render

from .forms import PostForm
from .models import Post


def post_list(request):
    """
    모든 Post목록을 리턴
    template은 'post/post_list.html'을 사용
    :param request:
    :return:
    """
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post/post_list.html', context)

def post_create(request):
    """
    Post를 생성
    반드시 photo필드에 해당하는 파일이 와야 한다
    :param request:
    :return:

    1. post_create.html파일을 만들고
        /post/create/ URL로 요청이 온 경우
        이 뷰에서 해당 파일은 render해서 response

    2. post_create.html form을 만들고
        file input과 button요소를 배치
        file input의 name은 'photo'로 지정

    3. 이 뷰에서 request.method가 'POST'일 경우
        request.POST와 request.FIlES를 print문으로 출력
        'GET'이면 템플릿 파일을 보여주는 기존 로직을 그대로 실행
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # 1. 파일이 오지 않았을 경우, GET 요청과 같은 결과를 리턴
        #   1-1. 단 return render(.....)하는 같은 함수를 두변 호출 하지 말 것
        if form.is_valid():
            print(form.cleand_data)
            post = Post.objects.create(
                photo=form.cleaned_data['photo'])
            return HttpResponse(f'<img src="{post.photo.url}">')
        else:
            return HttpResponse('Form invailid!')
    else:
        return render(request, 'post/post_create.html')

