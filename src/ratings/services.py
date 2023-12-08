from typing import List

from ratings.models import Rating
from users.models import User


class RatingService:
    @classmethod
    def create_rating(cls, user: User, **values: dict, ) -> None:
        comics = values["comics"]
        ratings = Rating.objects.filter(comics=comics)

        rating = ratings.filter(user=user).first()

        if isinstance(rating, Rating):
            rating.value = values["value"]
            rating.save()
        else:
            Rating.objects.create(user=user, **values)

        cls.update_comics_average_rating_value(ratings=ratings, comics=comics)

    @classmethod
    def update_comics_average_rating_value(cls, ratings: List[Rating], comics: dict) -> None:
        total_ratings = len(ratings)
        total_sum = sum(rating.value for rating in ratings)
        average_rating = total_sum / total_ratings if total_ratings > 0 else 0
        comics.rating = average_rating
        comics.save()
