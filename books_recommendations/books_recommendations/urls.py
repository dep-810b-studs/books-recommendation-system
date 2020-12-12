from django.urls import path
from books_recommendations.views import books_recommendations


urlpatterns = [
    path('', books_recommendations)
]
