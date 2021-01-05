import os
import pickle
import sys
from django.core.management import execute_from_command_line
from books_recommendations.recommendations_engine.hybrid_facto import HybridFacto

dump_path = './recommender.pkl'
with open(dump_path, 'rb') as dump_file:
    RECOMMENDATIONS_ENGINE = pickle.load(dump_file)

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books_recommendations.settings')
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
