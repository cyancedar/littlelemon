from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

def index(request):
  return render(request, 'index.html', {})

class MenuItemsView(ListCreateAPIView):
  permission_classes = [IsAuthenticated]
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
  permission_classes = [IsAuthenticated]
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer
  lookup_field = 'pk'

class BookingViewSet(ModelViewSet):
  permission_classes = [IsAuthenticated]
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer