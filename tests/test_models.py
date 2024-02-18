from django.test import TestCase
from django.urls import reverse
from restaurant.models import Menu
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User


class MenuTest(TestCase):
  def test_get_item(self):
    item = Menu.objects.create(title="Ice Cream", price= 2, inventory=100)
    created_item = Menu.objects.get(title="Ice Cream")
    self.assertEqual(created_item.title, "Ice Cream")
    self.assertEqual(created_item.price, 2)
    self.assertEqual(created_item.inventory, 100)

class MenuViewTest(TestCase):
  def setUp(self):
    Menu.objects.create(title="Burger", price=10.00, inventory=50)
    Menu.objects.create(title="Fries", price=5.00, inventory=100)
    self.user = User.objects.create_user(username='testuser', password='testpassword')

  def test_getall(self):
    self.client = APIClient()
    self.client.login(username='testuser', password='testpassword')
    response = self.client.get(reverse('menu-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    queryset = Menu.objects.all()
    serializer = MenuSerializer(queryset, many=True)
    self.assertEqual(response.data, serializer.data)