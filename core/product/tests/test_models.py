from django.test import TestCase
from product.models import Brand, Product


class TestBrandModel(TestCase):

    def test_model_str_method(self):
        brand = Brand.objects.create(title='samsung', nationality='korea')
        self.assertEqual(str(brand), 'samsung')


class TestProductModel(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(title='samsung', nationality='korea')

    def test_model_str_method(self):
        product = Product.objects.create(
            brand=self.brand,
            title='galaxy',
            price=1000,
            screen_size=6.5,
            color='white',
            made_in='korea',
        )
        self.assertEqual(str(product), 'galaxy')
