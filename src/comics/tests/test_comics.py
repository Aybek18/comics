from typing import List

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from comics.tests.factories import ComicsFactory
from users.tests.factories import UserFactory


@pytest.mark.django_db
class TestListComics:
    url = reverse("comics-list")

    def test_throws_error_if_access_token_invalid(self, api_client: APIClient) -> None:
        access_token = "NotValidAccessToken"
        api_client.credentials(HTTP_AUTHORIZATION=f"Token {access_token}")
        response = api_client.get(self.url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_returns_list_comics(self, api_client: APIClient, user: UserFactory,
                                 list_comics: List[ComicsFactory]) -> None:
        access_token, _ = Token.objects.get_or_create(user=user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Token {access_token.key}")
        response = api_client.get(self.url)

        assert response.status_code == status.HTTP_200_OK


class TestComicsRetrieve:

    def get_url(self, bookmark_id: int = 12345):
        return reverse("comics-retrieve", args=[bookmark_id])

    def test_throws_error_if_access_token_invalid(self, api_client: APIClient, comics: ComicsFactory) -> None:
        access_token = "NotValidAccessToken"
        api_client.credentials(HTTP_AUTHORIZATION=f"Token {access_token}")
        response = api_client.get(self.get_url(comics.id))
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_return_404_if_comics_doesnt_exist(self, api_client: APIClient, user: UserFactory) -> None:
        access_token, _ = Token.objects.get_or_create(user=user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Token {access_token.key}")
        response = api_client.get(self.get_url(10000))

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() == {
            "detail": "Comics with this ID doesn't exist"
        }

    def test_return_comics(self, api_client: APIClient, user: UserFactory, comics: ComicsFactory) -> None:
        access_token, _ = Token.objects.get_or_create(user=user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Token {access_token.key}")
        response = api_client.get(self.get_url(comics.id))
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            "id": comics.id,
            "title": comics.title,
            "author": comics.author,
            "rating": comics.rating
        }
