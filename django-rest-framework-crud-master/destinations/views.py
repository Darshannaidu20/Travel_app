from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Destination
from .permissions import IsOwnerOrReadOnly
from .serializers import DestinationSerializer
from .pagination import CustomPagination
from .filters import DestinationFilter





from rest_framework.exceptions import NotFound, ValidationError, PermissionDenied
from rest_framework.response import Response
from rest_framework.views import exception_handler

class CustomException(Exception):
    def __init__(self, detail, status_code):
        self.detail = detail
        self.status_code = status_code

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, CustomException):
        return Response(data={'error': exc.detail}, status=exc.status_code)

    return response

class ListCreateDestinationAPIView(ListCreateAPIView):

    """
    View for listing and creating destinations.

    Permissions:
    - Only authenticated users are allowed.

    Query Parameters:
    - Supports filtering by various fields using query parameters.

    Pagination:
    - Paginated response with custom pagination class.
    """
    
    serializer_class = DestinationSerializer
    queryset = Destination.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DestinationFilter

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)  # Ensure serializer is valid before saving
        serializer.save(creator=self.request.user)

class RetrieveUpdateDestroyDestinationAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DestinationSerializer
    queryset = Destination.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]  

    def perform_update(self, serializer):
        serializer.is_valid(raise_exception=True)  # Ensure serializer is valid before saving
        serializer.save()



