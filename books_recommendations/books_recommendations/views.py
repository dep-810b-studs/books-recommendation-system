from django.shortcuts import render


def books_recommendations(request):
    return render(request, "BooksRecommendations.html", {})