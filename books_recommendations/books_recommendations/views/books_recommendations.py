import pickle

from django.shortcuts import render
from django.views.generic import TemplateView

from books_recommendations.forms import BookForm
from books_recommendations.settings import BASE_VIEWS_FOLDER, BASE_DIR
from manage import RECOMMENDATIONS_ENGINE


class BooksRecommendationsView(TemplateView):
    """View class for page with books recommendations"""

    def __init__(self):
        self.__default_view = "BooksRecommendations.html"

    def get(self, request, *args, **kwargs):
        book_form = BookForm()
        books_context = {
           'rating_prediction': 0.0,
           'book_form': book_form
        }

        return render(request, f'{BASE_VIEWS_FOLDER}/{self.__default_view}', books_context)

    def post(self, request, *args, **kwargs):
        book_form = BookForm(request.POST)
        user_id = book_form.data.get('user_id')
        book_id = book_form.data.get('book_id')

        if user_id.isdigit() and book_id.isdigit():
            user_id, book_id = int(user_id), int(book_id)
            current_rating_prediction = RECOMMENDATIONS_ENGINE.estimate([(user_id, book_id, 0)])
        else:
            current_rating_prediction = None

        books_context = {
            'book_form': book_form,
            'rating_prediction': current_rating_prediction
        }
        return render(request, f'{BASE_VIEWS_FOLDER}/{self.__default_view}', books_context)

