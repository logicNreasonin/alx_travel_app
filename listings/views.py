from rest_framework import viewsets
# from rest_framework import permissions # If you want to add permissions
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows listings to be viewed or edited.
    Provides GET (list, retrieve), POST, PUT, PATCH, DELETE actions.
    """
    queryset = Listing.objects.all().order_by('-created_at')
    serializer_class = ListingSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Example permission


class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bookings to be viewed or edited.
    Provides GET (list, retrieve), POST, PUT, PATCH, DELETE actions.
    """
    queryset = Booking.objects.all().order_by('-created_at')
    serializer_class = BookingSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Example permission

    # You could add custom logic, e.g., to filter bookings by user:
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         return Booking.objects.filter(guest=user).order_by('-created_at')
    #     return Booking.objects.none() # Or all if admin, or raise error