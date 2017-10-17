from django.contrib.auth import authenticate, login as django_login, get_user_model
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import UserForm

User = get_user_model()

def login(request):
    # POST요청 (Form subit)의 경우
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(
                username=username,
                password=password
            )
            if user is not None:
                django_login(request, user)
                return redirect('post_list')
            else:
                return HttpResponse('로그인 실패. 다시 시도 해보세요')
    else:
        return render(request, 'member/login.html')


def signup(request):

    if request.method == 'POST':
        # 데이터가 binding 된 SignupForm 인스턴스를 생성 (bound 된 form 이다)
        user_form = UserForm(request.POST)
        # 해당 form이 자신의 필드에 유효한 데이터를 가지고 있는지 유효성 검사 -> True를 반환하면

        if user_form.is_valid():
            # 통과한 경우 정제된 데이터 (cleaned_data)에서  username과 password 를
            # form 에서 데이터를 변형시킬수도 있다.(에를 들면 전화번호에 000-0000-0000 변형하고 싶을때 )
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']

            if username and password:
                if User.objects.filter(username=username).exists():
                    return HttpResponse(f'Username {username} is already exist')

                user = User.objects.create_user(
                    username=username,
                    password=password,
                )
                user.save()
                return HttpResponse(f'{user.username}, {user.password}')
    # get 요청일 때는 Signup
    else:
        user_form = UserForm()

    context = {
        'user_form': user_form,

    }
    return render(request, 'member/signup.html', context)




