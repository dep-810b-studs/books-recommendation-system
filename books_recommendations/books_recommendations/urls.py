from django.urls import path
from books_recommendations.views.books_recommendations import BooksRecommendationsView
from books_recommendations.views.recommendations_engine import RecommendationsEngineView

urlpatterns = [
    path('', BooksRecommendationsView.as_view()),
    path('engine', RecommendationsEngineView.as_view())
]
