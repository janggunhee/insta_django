from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from member.form import UserForm


def signup(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST)

        # 조건에 objects의 query를 이용해서 중복을 막기
        # 이미 해당 User가 존재하는지 검사

        if user_form.is_valid():
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
    else:
        user_form = UserForm()

    context = {
        'user_form': user_form,

    }
    return render(request, 'member/signup.html', context)




