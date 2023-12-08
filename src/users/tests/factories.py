import factory

from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker("pystr")
    password = factory.PostGenerationMethodCall("set_password", "password123")

    class Meta:
        model = User
