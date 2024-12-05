from django.shortcuts import render


# Create your views here.
def platform(request):
    title = 'Мой сайт'
    header = 'Главная страница'
    context = {"title": title,
               "header": header
               }
    return render(request, 'platform.html', context)


def games(request):
    title = 'Магазин'
    header = 'Игры'
    games_list = ["Atomic Heart", "Cyberpunk 2077", "PayDay 2"]
    context = {"title": title,
               "header": header,
               "games_list": games_list
               }
    return render(request, 'games.html', context)


def cart(request):
    title = 'Корзина'
    header = 'Корзина'
    message = 'Извините, Ваша корзина пуста'
    context = {"title": title,
               "header": header,
               "message": message
               }
    return render(request, 'cart.html', context)
