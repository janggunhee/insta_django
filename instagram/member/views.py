from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from member.form import UserForm


def signup(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            user = User.objects.create_user(
                username=username,
                password=password,
            )
            user.save()
        return HttpResponse(f'{a.username}, {a.password}')
    else:
        user_form = UserForm()


    context = {
        'user_form': user_form,

    }
    return render(request, 'member/signup.html', context)




