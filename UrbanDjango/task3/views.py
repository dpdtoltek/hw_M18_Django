from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def platform(request):
    data = {"title": "Мой сайт", "header": "Главная страница", "menu1": "Главная", "menu2": "Магазин",
            "menu3": "Корзина", "come back": "Вернуться обратно"}
    return render(request, 'platform.html', context=data)


def games(request):
    data = {"title": "Магазин", "header": "Игры", "game1": "Atomic Heart", "game2": "Cyberpunk 2077", "game3":
            "PayDay 2", "come_back": "Вернуться обратно"}
    return render(request, 'games.html', context=data)


def cart(request):
    data = {"title": "Корзина", "message": "Извините, Ваша корзина пуста", "come_back": "Вернуться обратно"}
    return render(request, 'cart.html', context=data)
