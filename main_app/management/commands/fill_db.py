

from django.core.management.base import BaseCommand
from main_app.models import *
from datetime import date

class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        news= [
            {'type_news': 'Программирование'},
            {'type_news': 'Железо'},
            {'type_news': 'Смартфоны'},
        ]



        for new in news:
            new = Type_news(**new)
            new.save()


