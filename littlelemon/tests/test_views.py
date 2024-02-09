
from django.test import TestCase, RequestFactory
from restaurant.models import Menu
from restaurant.views import MenuItemView


class MenuViewTest(TestCase):
    def setUp(self):
        menu_item = Menu.objects.create(title="Coffe", price=80, inventory=100)
        return super().setUp()

    def test_getall(self):
        request = RequestFactory().get('/restaurant/menu')
        view = MenuItemView()
        view.setup(request)

        context = str(view.get_queryset())
        self.assertIn('Coffe : 80.00', context)