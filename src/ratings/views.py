from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from ratings.serializers import RatingSerializer
from ratings.services import RatingService


class RatingAPIView(CreateAPIView):
    serializer_class = RatingSerializer

    @extend_schema(
        responses={201: OpenApiResponse(description='{"message": "Рейтинг добавлен"}')})
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.request.user
        RatingService.create_rating(user=user, **serializer.validated_data)
        return Response({"message": "Рейтинг добавлен"}, status=status.HTTP_200_OK)
