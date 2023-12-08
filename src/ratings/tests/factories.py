import factory
from faker import Faker

from comics.tests.factories import ComicsFactory
from ratings.models import Rating
from users.tests.factories import UserFactory


class RatingFactory(factory.django.DjangoModelFactory):
    value = Faker().random_int(min=1, max=5)
    user = factory.SubFactory(UserFactory)
    comics = factory.SubFactory(ComicsFactory)

    class Meta:
        model = Rating
