from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

users = [
    {'username': 'Nika', 'password': 'abc1234', 'age': 25},
    {'username': 'Oleg', 'password': 'def567', 'age': 36},
    {'username': 'Sasha', 'password': 'rew89', 'age': 40}
    ]
info = {}


# Create your views here.
def sign_up_by_django(request):
    usernames = [user['username'] for user in users]
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password == repeat_password and age >= 18 and username not in usernames:
                return HttpResponse(f'Приветствуем, {username}!')
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'registration_page.html', context=info)
                # return HttpResponse('Пароли не совпадают')
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'registration_page.html', context=info)
            elif username in usernames:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'registration_page.html', context=info)
        else:
            info['error'] = 'Некорректный ввод данных'
            return render(request, 'registration_page.html', context=info)
    else:
        form = UserRegister()

    return render(request, 'registration_page.html', {'form': form})


def sign_up_by_html(request):
    usernames = [user['username'] for user in users]
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        if password == repeat_password and age >= 18 and username not in usernames:
            return HttpResponse(f'Приветствуем, {username}!')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return render(request, 'registration_page.html', context=info)
            # return HttpResponse('Пароли не совпадают')
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
            return render(request, 'registration_page.html', context=info)
        elif username in usernames:
            info['error'] = 'Пользователь уже существует'
            return render(request, 'registration_page.html', context=info)
    return render(request, 'registration_page.html')
