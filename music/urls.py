from django.urls import path
from .views import SongListView, RadioStationListView

urlpatterns = [
    path("songs/", SongListView.as_view(), name="songs"),
    path("radio-stations/", RadioStationListView.as_view(), name="radio-stations"),
]
