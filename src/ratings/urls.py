from django.urls import path

from ratings.views import RatingAPIView

urlpatterns = [
    path("", RatingAPIView.as_view(), name="rating-create"),

]