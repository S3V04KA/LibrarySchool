from django.urls import path
from . import views

urlpatterns = [
    path('librarian', views.home_librarian, name='main'),
    path('librarian/management', views.fund_management, name='management'),
    path('librarian/management/add_book', views.create_book, name='add_book'),
    path('librarian/management/change', views.edit_book, name='change_book'),
    path('librarian/control', views.control_extradition, name='control'),
    path('librarian/control/students_initials', views.students_initials, name='initials'),
    path('librarian/control/date', views.date_of_issue, name='date_of_issue'),
    path('librarian/control/author', views.author_choice, name='author_choice'),
    path('librarian/control/class', views.class_choice, name='class_choice'),
    path('librarian/debts', views.debts, name='debts')
    ]
