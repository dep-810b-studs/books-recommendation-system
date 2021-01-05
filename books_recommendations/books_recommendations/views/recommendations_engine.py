from django.http import FileResponse
from django.views.generic import TemplateView

from books_recommendations.settings import BASE_DIR


class RecommendationsEngineView(TemplateView):
    """View class for page with jupyter notebook with engine of system"""

    def __init__(self):
        self.__path = f"{BASE_DIR}/templates/books_recommendations/RecommendationsEngine.pdf"

    def get(self, request, *args, **kwargs):
        return FileResponse(open(self.__path, 'rb'), content_type='application/pdf')
