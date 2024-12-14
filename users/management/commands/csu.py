from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = 'Команда для заполнения таблицы в БД'
    def handle(self, *args, **options):
        user = User.objects.create(email="admin@example.com")
        user.first_name = 'admin',
        user.last_name = 'admin',
        user.is_staff = True
        user.is_superuser = True

        user.set_password("123qwerty")
        user.save()
        