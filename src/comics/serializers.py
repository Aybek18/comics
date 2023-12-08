from rest_framework import serializers

from comics.models import Comics


class ComicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comics
        fields = ('id', 'title', 'author', 'rating')
