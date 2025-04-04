from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_library, name='home'),
    path('login/', views.login, name='login'),
    path('notifications', views.notifications, name = 'notifications'),
    path('mylibrary/', views.library_for_user, name='mylibrary'),
    path('mylibrary/favorites', views.favorites, name='favorites'),
    path('mylibrary/history', views.order_history, name='order_history'),
    path('mylibrary/history/returnBook/', views.return_the_book, name='return_the_book'),
    path('mylibrary/history/returnBook/scannerQR', views.qr_code_scanner_return, name='scanner_return'),
    path('about/', views.about_the_library, name='about'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('recommendations/choice', views.choice_books, name='choice1'),
    path('search/', views.search, name='search'),
    path('search/description/', views.get_book_description, name='get_book_search_description'),
    path('search/description/scannerQR', views.qr_code_scanner_search_get, name='scannerQR_search_get'),
    path('search/choice', views.choice_books, name='choice2'),
    path('search/new/', views.new_books, name='new_books'),
    path('search/new/description/', views.new_books_description, name='new_books_description'),
    path('search/new/description/scannerQR', views.qr_code_scanner_new_get, name='scannerQR_new_get'),
    path('search/filter/', views.filter_book, name='filter_book'),
    path('search/filter/genres', views.genre_of_the_book, name='genre_of_the_book'),
    path('search/filter/disciplines', views.academic_disciplines, name='academic_disciplines'),
    path('search/filter/results/', views.filter_search_results, name='filter_search_results'),
    path('search/filter/results/description/', views.filter_results_description, name='filter_results_description'),
    path('search/filter/results/description/scannerQR', views.qr_code_filter_results_description, name='scannerQR_filter_results')
]