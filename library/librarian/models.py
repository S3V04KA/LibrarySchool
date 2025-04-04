from django.db import models

class A(models.Model):
    title = models.CharField('Название', max_length=50)
    author = models.CharField('Автор', max_length=50)
    genre = models.CharField('Жанр', max_length=50)
    description = models.TextField('Описание книги', max_length=100)
    number_of_copies = models.TextField('Количество экземпляров', max_length=50)
    date = models.CharField('Дата', max_length=50)

    def __str__(self):
        return f"Новость - {self.title}"

    def get_absolute_url(self):
        return f'/librarian/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'