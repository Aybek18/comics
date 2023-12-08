import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from comics.tests.factories import ComicsFactory
from users.tests.factories import UserFactory


@pytest.mark.django_db
class TestRating:
    url = reverse("rating-create")

    def test_requires_fields(self, api_client: APIClient, user: UserFactory) -> None:
        access_token, _ = Token.objects.get_or_create(user=user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Token {access_token.key}")

        response = api_client.post(self.url)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == {
            "comics": [
                "This field is required."
            ],
            "value": [
                "This field is required."
            ]
        }

    def test_throws_error_if_access_token_invalid(self, api_client: APIClient) -> None:
        access_token = "NotValidAccessToken"
        api_client.credentials(HTTP_AUTHORIZATION=f"Token {access_token}")
        response = api_client.post(self.url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_return_400_if_comics_doesnt_exist(self, api_client: APIClient, user: UserFactory) -> None:
        data = {
            "comics": 1000,
            "value": 1
        }

        access_token, _ = Token.objects.get_or_create(user=user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Token {access_token.key}")
        response = api_client.post(self.url, data=data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == {'comics': [f'Invalid pk "{data["comics"]}" - object does not exist.']}

    def test_creates_rating(self, api_client: APIClient, user: UserFactory, comics: ComicsFactory) -> None:
        data = {
            "comics": comics.id,
            "value": 1
        }

        access_token, _ = Token.objects.get_or_create(user=user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Token {access_token.key}")
        response = api_client.post(self.url, data=data)

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {'message': 'Рейтинг добавлен'}

