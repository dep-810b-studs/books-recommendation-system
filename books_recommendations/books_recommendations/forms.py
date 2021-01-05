from django.forms import Form, TextInput, IntegerField


class BookForm(Form):
    user_id = IntegerField(label='user_id', widget=TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите id пользователя'
            }))
    book_id = IntegerField(label='book_id', widget=TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите id книги'
            }))