from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Song, RadioStation
from .serializers import SongSerializer, RadioStationSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Custom pagination class for handling pagination in API views


class SongPagination(PageNumberPagination):
    page_size = 10  # 10 items per page
    # Allow users to specify page size via query param
    page_size_query_param = 'page_size'
    max_page_size = 100  # Max page size limit

# Song List View with filtering, pagination, and ordering


class SongListView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = SongPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['title', 'artist', 'genre']
    ordering_fields = ['title', 'artist', 'release_date']
    ordering = ['title']

    @swagger_auto_schema(
        operation_description="Retrieve a list of songs with filtering and pagination.",
        responses={200: SongSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter('title', openapi.IN_QUERY,
                              description="Filter songs by title", type=openapi.TYPE_STRING),
            openapi.Parameter('artist', openapi.IN_QUERY,
                              description="Filter songs by artist", type=openapi.TYPE_STRING),
            openapi.Parameter('genre', openapi.IN_QUERY,
                              description="Filter songs by genre", type=openapi.TYPE_STRING),
            openapi.Parameter('ordering', openapi.IN_QUERY,
                              description="Order by specific fields", type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

# Radio Station List View with filtering and pagination


class RadioStationListView(generics.ListAPIView):
    queryset = RadioStation.objects.all()
    serializer_class = RadioStationSerializer
    pagination_class = SongPagination  # Reuse the same pagination class
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['name']
    ordering_fields = ['name']
    ordering = ['name']

    @swagger_auto_schema(
        operation_description="Retrieve a list of radio stations with filtering and pagination.",
        responses={200: RadioStationSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter('name', openapi.IN_QUERY,
                              description="Filter radio stations by name", type=openapi.TYPE_STRING),
            openapi.Parameter('ordering', openapi.IN_QUERY,
                              description="Order by specific fields", type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
