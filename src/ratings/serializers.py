from rest_framework import serializers

from ratings.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'comics', 'user', 'value')
        read_only_fields = ("user", )
