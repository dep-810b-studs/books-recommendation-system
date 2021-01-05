import os
import sys
from django.core.management import execute_from_command_line
from books_recommendations.recommendations_engine.hybrid_facto import HybridFacto

RECOMMENDATIONS_ENGINE = HybridFacto.load_instance_from_dump()


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books_recommendations.settings')
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
