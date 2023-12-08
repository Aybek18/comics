import factory
from faker import Faker

from comics.models import Comics


class ComicsFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("sentence")
    author = factory.Faker("name")
    rating = Faker().pyfloat(min_value=1.00, max_value=5.00)

    class Meta:
        model = Comics
