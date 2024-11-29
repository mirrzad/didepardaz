from django.test import TestCase
from product.forms import AddProductForm
from product.models import Brand, Product


class TestAddProductForm(TestCase):

    def setUp(self):
        self.brand = Brand.objects.create(title='samsung', nationality='korea')
        self.product = Product.objects.create(
            brand=self.brand,
            title='galaxy s23',
            price=1200,
            screen_size=6.5,
            color='white',
            made_in='korea',
        )

    def test_valid_data(self):
        form = AddProductForm(data={
            'brand': self.brand,
            'title': 'galaxy',
            'price': 1000,
            'color': 'white',
            'screen_size': 6.5,
            'is_available': True,
            'made_in': 'korea',
        })
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = AddProductForm(data={
            'brand': self.brand,
            'title': 'galaxy',
            'price': 1000,
            'screen_size': 6.5,
            'is_available': 'test',
            'made_in': 'korea',
        })
        self.assertEqual(len(form.errors), 1)
        self.assertTrue(form.has_error('color'))

    def test_unique_title(self):
        form = AddProductForm(data={
            'brand': self.brand,
            'title': 'galaxy s23',
            'price': 1000,
            'screen_size': 6.5,
            'is_available': 'test',
            'made_in': 'korea',
        })
        self.assertTrue(form.has_error('title'))

