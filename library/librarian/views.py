from .form import AForm
from django.shortcuts import redirect
from django.shortcuts import render


def home_librarian(request):
    data = {
        'title':'Библиотекарь'
    }
    return render(request, 'librarian/home_librarian.html', data)
def fund_management(request):
    data = {
        'title':'Управление фондом'
    }
    return render(request, 'librarian/management.html', data)
def add_book(request):
    data = {
        'title': 'Добавить книгу'
    }
    return render(request, 'librarian/add_book.html', data)
def change_book(request):
    data = {
        'title': 'Редактировать книгу'
    }
    return render(request, 'librarian/change_book.html', data)
def control_extradition(request):
    data = {
        'title': 'Мониторинг выдачи'
    }
    return render(request, 'librarian/control_extradition.html', data)
def students_initials(request):
    data = {
        'title': 'ФИО Ученика'
    }
    return render(request, 'librarian/students_initials.html', data)
def date_of_issue(request):
    data = {
        'title': 'Дата выдачи'
    }
    return render(request, 'librarian/date_of_issue.html', data)
def author_choice(request):
    data = {
        'title': 'По автору'
    }
    return render(request, 'librarian/author_choice.html', data)
def class_choice(request):
    data = {
        'title': 'По классу'
    }
    return render(request, 'librarian/class_choice.html', data)
def debts(request):
    data = {
        'title': 'Управление задолженностями',
        't1': 'Список должников'
    }
    return render(request, 'librarian/debts.html', data)
def create_book(request):
    error = ''
    if request.method == 'POST':
        form = AForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'false data'
    form = AForm()
    data = {
        'title': 'Добавить книгу',
        'form': form,
        'error': error
    }
    return render(request, 'librarian/add_book.html', data)
def edit_book(request):

    if request.method == 'PUT':
        form = AForm(request.PUT)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = AForm()

    return render(request, 'librarian/change_book.html', {'form': form})