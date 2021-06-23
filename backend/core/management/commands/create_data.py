from random import choices

from django.conf import settings
from django.core.management.base import BaseCommand
from faker import Faker

from backend.call.constants import STATUS
from backend.call.models import Call, Category, Subcategory
from backend.utils import utils as u
from backend.utils.progress_bar import progressbar
from backend.utils.read_csv import csv_to_list

fake = Faker()


def get_user():
    first_name = u.gen_first_name()
    last_name = u.gen_last_name()
    d = dict(
        first_name=first_name,
        last_name=last_name,
        email=u.gen_email(first_name, last_name),
    )
    return d


def data_category():
    filename = settings.BASE_DIR.joinpath('backend/fixtures/categories.csv')
    return csv_to_list(filename)


def create_category():
    Category.objects.all().delete()
    aux_list = []
    categories = data_category()
    for item in progressbar(categories, 'Category'):
        data = {'title': item['title']}
        obj = Category(**data)
        aux_list.append(obj)
    Category.objects.bulk_create(aux_list)


def data_subcategory():
    filename = settings.BASE_DIR.joinpath('backend/fixtures/subcategories.csv')
    return csv_to_list(filename)


def get_subcategory(item):
    category = Category.objects.get(title=item['category'])
    d = dict(
        title=item['title'],
        category=category,
    )
    return d


def create_subcategory():
    Subcategory.objects.all().delete()
    aux_list = []
    subcategories = data_subcategory()
    for item in progressbar(subcategories, 'Subcategory'):
        data = get_subcategory(item)
        obj = Subcategory(**data)
        aux_list.append(obj)
    Subcategory.objects.bulk_create(aux_list)


def get_call():
    d = dict(
        title=u.gen_title(nb_words=7, remove_dot=True),
        description=u.gen_text(),
        status=choices(STATUS)[0][0],
    )
    return d


def create_call():
    Call.objects.all().delete()
    aux_list = []
    for item in progressbar(range(100), 'Call'):
        data = get_call()
        obj = Call(**data)
        aux_list.append(obj)
    Call.objects.bulk_create(aux_list)


class Command(BaseCommand):
    help = 'Create data.'

    def handle(self, *args, **options):
        self.stdout.write('Create data.')
        create_category()
        create_subcategory()
        create_call()
