from django.http import HttpResponse
from django.shortcuts import render

def home_library(request):
    data = {
        'title':'Главная страница'
    }
    return render(request, 'home/home_library.html', data)
def notifications(request):
    data = {
        'title': 'Уведомления'
    }
    return render(request, 'home/notifications.html', data)
def library_for_user(request):
    data = {
        'title': 'Моя библиотека'
    }
    return render(request, 'home/library_for_user.html', data)
def favorites(request):
    data = {
        'title': 'Избранное'
    }
    return render(request, 'home/favorites.html', data)
def get_book_description(request):
    data = {
        'title': 'Описание книги'
    }
    return render(request, 'home/get_book_description.html', data)
def order_history(request):
    data = {
        'title': 'История заказов'
    }
    return render(request, 'home/order_history.html', data)
def return_the_book(request):
    data = {
        'title':'Возврат книги',
        't1': 'Для того чтобы вернуть книгу, сканируйте QR-код'
    }
    return render(request, 'home/return_the_book.html', data)
def qr_code_scanner_search_get(request):
    data = {
        'title':'Сканирование QR-кода'
    }
    return render(request, 'home/scannerQR_search_get.html', data)
def qr_code_scanner_return(request):
    data = {
        'title':'Сканирование QR-кода'
    }
    return render(request, 'home/scannerQR_return.html', data)
def about_the_library(request):
    data = {
        'title': 'О библиотеке'
    }
    return render(request, 'home/about.html', data)
def recommendations(request):
    data = {
        'title': 'Рекомендации'
    }
    return render(request, 'home/recommendations.html', data)
def search(request):
    data = {
        'title': 'Поиск книг'
    }
    return render(request, 'home/search.html', data)
def new_books(request):
    data = {
        'title': 'Новинки'
    }
    return render(request, 'home/new_books.html', data)
def new_books_description(request):
    data = {
        'title': 'Описание книги'
    }
    return render(request, 'home/new_books_description.html', data)
def qr_code_scanner_new_get(request):
    data = {
        'title': 'Получить книгу'
    }
    return render(request, 'home/scannerQR_new_get.html', data)
def filter_book(request):
    data = {
        'title': 'Настроить фильтр'
    }
    return render(request, 'home/filter_book.html', data)
def genre_of_the_book(request):
    data = {
        'title': 'Жанр'
    }
    return render(request, 'home/genre_of_the_book.html', data)
def academic_disciplines(request):
    data = {
        'title': 'Предметы'
    }
    return render(request, 'home/academic_disciplines.html', data)
def filter_search_results(request):
    data = {
        'title': 'Результаты поиска'
    }
    return render(request, 'home/filter_search_results.html', data)
def filter_results_description(request):
    data = {
        'title': 'Описание книги'
    }
    return render(request, 'home/filter_results_description.html', data)
def qr_code_filter_results_description(request):
    data = {
        'title': 'Сканирование QR-кода'
    }
    return render(request, 'home/scannerQR_filter_results.html', data)
def choice_books(request):
    data = {
        'title': 'Выбор книги'
    }
    return render(request, 'home/choice.html', data)
def login():
    return HttpResponse("Авторизация")
