from random import choices

from django.conf import settings
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
from django.db.models import Q
from faker import Faker

from backend.accounts.models import User
from backend.call.constants import STATUS
from backend.call.models import Call, Category, Subcategory
from backend.utils import utils as u
from backend.utils.progress_bar import progressbar
from backend.utils.read_csv import csv_to_list

fake = Faker()


def create_groups():
    Group.objects.all().delete()
    groups = ['Gestor', 'Suporte', 'Padrão']
    aux_list = []

    for group in progressbar(groups, 'Groups'):
        obj = Group(name=group)
        aux_list.append(obj)

    Group.objects.bulk_create(aux_list)


def get_user():
    first_name = u.gen_first_name()
    last_name = u.gen_last_name()
    d = dict(
        first_name=first_name,
        last_name=last_name,
        email=u.gen_email(first_name, last_name),
    )
    return d


def create_users():
    User.objects.exclude(
        Q(email='admin@email.com') |
        Q(email='regis@email.com')
    ).delete()
    aux_list = []

    for _ in progressbar(range(10), 'Users'):
        data = get_user()
        obj = User(**data)
        aux_list.append(obj)

    User.objects.bulk_create(aux_list)


def add_group_on_user():
    users = User.objects.exclude(
        Q(email='admin@email.com') |
        Q(email='regis@email.com')
    )
    groups = Group.objects.all()

    for user in progressbar(users, 'Add Group on Users'):
        group = choices(groups)[0]
        user.groups.add(group)

    user = User.objects.get(email='regis@email.com')
    user.groups.add(Group.objects.get(name='Gestor'))


def data_category():
    filename = settings.BASE_DIR.joinpath('backend/fixtures/categories.csv')
    return csv_to_list(filename)


def create_categories():
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


def create_subcategories():
    Subcategory.objects.all().delete()
    aux_list = []
    subcategories = data_subcategory()

    for item in progressbar(subcategories, 'Subcategory'):
        data = get_subcategory(item)
        obj = Subcategory(**data)
        aux_list.append(obj)

    Subcategory.objects.bulk_create(aux_list)


def get_call():
    users = User.objects.exclude(email='admin@email.com')
    subcategories = Subcategory.objects.all()
    d = dict(
        title=u.gen_title(nb_words=7, remove_dot=True),
        description=u.gen_text(),
        status=choices(STATUS)[0][0],
        user=choices(users)[0],
        subcategory=choices(subcategories)[0],
    )
    return d


def create_calls():
    Call.objects.all().delete()
    aux_list = []

    for item in progressbar(range(200), 'Call'):
        data = get_call()
        obj = Call(**data)
        aux_list.append(obj)

    Call.objects.bulk_create(aux_list)


class Command(BaseCommand):
    help = 'Create data.'

    def handle(self, *args, **options):
        self.stdout.write('Create data.')
        create_groups()
        create_users()
        add_group_on_user()
        create_categories()
        create_subcategories()
        create_calls()
