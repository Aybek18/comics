from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveAPIView

from comics.models import Comics
from comics.serializers import ComicsSerializer


class ComicsListAPIView(ListAPIView):
    serializer_class = ComicsSerializer
    queryset = Comics.objects.all()


class ComicsRetrieveAPIView(RetrieveAPIView):
    serializer_class = ComicsSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        try:
            return Comics.objects.get(pk=pk)
        except Comics.DoesNotExist:
            raise NotFound("Comics with this ID doesn't exist")
