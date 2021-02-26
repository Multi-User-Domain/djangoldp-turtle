import uuid
from djangoldp.tests.models import User


def get_random_user(is_superuser=False):
    return User.objects.create(email='{}@test.co.uk'.format(str(uuid.uuid4())), first_name='Test',
                               last_name='Test', username=str(uuid.uuid4()), is_superuser=is_superuser)
