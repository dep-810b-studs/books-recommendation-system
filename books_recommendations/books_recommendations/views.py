from django.shortcuts import render


def books_recommendations(request):
    return render(request, "books_recommendations/BooksRecommendations.html", {})