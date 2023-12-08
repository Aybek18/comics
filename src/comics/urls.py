from django.urls import path

from comics.views import ComicsListAPIView, ComicsRetrieveAPIView

urlpatterns = [
    path("", ComicsListAPIView.as_view(), name="comics-list"),
    path("<int:pk>", ComicsRetrieveAPIView.as_view(), name="comics-retrieve"),
]