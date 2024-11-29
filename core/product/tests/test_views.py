from django.test import TestCase, Client
from django.urls import reverse
from product.models import Brand, Product
from product.forms import AddProductForm, AddBrandForm, BrandFilterForm


class TestAddBrandView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_GET_method(self):
        res = self.client.get(reverse('product:add-brand'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'product/add-brand.html')
        self.assertEqual(res.context['form'], AddBrandForm)

    def test_POST_method_valid(self):
        res = self.client.post(reverse('product:add-brand'), data={'title': 'samsung', 'nationality': 'korea'})
        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, reverse('product:add-brand'))
        self.assertEqual(Brand.objects.count(), 1)

    def test_POST_method_invalid(self):
        res = self.client.post(reverse('product:add-brand'), data={})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(Brand.objects.count(), 0)
        self.assertFalse(res.context['form'].is_valid())


class TestAddProductView(TestCase):
    def setUp(self):
        self.client = Client()
        self.brand = Brand.objects.create(title='samsung', nationality='korea')

    def test_GET_method(self):
        res = self.client.get(reverse('product:add-product'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'product/add-product.html')
        self.assertEqual(res.context['form'], AddProductForm)

    def test_POST_method_valid(self):
        res = self.client.post(reverse('product:add-product'),
                               data={
                                   'brand': self.brand.id,
                                   'title': 'galaxy s25',
                                   'price': 1000,
                                   'color': 'white',
                                   'screen_size': 6.5,
                                   'is_available': True,
                                   'made_in': 'korea',
                               })

        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, reverse('product:add-product'))
        self.assertEqual(Product.objects.count(), 1)

    def test_POST_method_invalid(self):
        res = self.client.post(reverse('product:add-product'), data={})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(Product.objects.count(), 0)
        self.assertFalse(res.context['form'].is_valid())


class TestBrandReport(TestCase):
    def setUp(self):
        self.client = Client()
        self.brand = Brand.objects.create(title='samsung', nationality='korea')

    def test_GET_method(self):
        res = self.client.get(reverse('product:report-brand'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'product/brand-report.html')
        self.assertEqual(len(res.context['brands']), 1)


class TestProductReport(TestCase):
    def setUp(self):
        self.client = Client()
        self.brand = Brand.objects.create(title='samsung', nationality='korea')
        self.product = Product.objects.create(
            brand=self.brand,
            title='galaxy s23',
            price=1200,
            screen_size=6.5,
            color='white',
            made_in='korea',
        )

    def test_GET_method(self):
        res = self.client.get(reverse('product:report-product'), data={'brand': self.brand.id})
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'product/product-report.html')
        self.assertEqual(len(res.context['products']), 1)
        self.assertEqual(res.context['form'], BrandFilterForm)


class TestProductMadeInNationEqualReport(TestCase):
    def setUp(self):
        self.client = Client()
        self.brand = Brand.objects.create(title='samsung', nationality='korea')
        self.product = Product.objects.create(
            brand=self.brand,
            title='galaxy s23',
            price=1200,
            screen_size=6.5,
            color='white',
            made_in='korea',
        )

    def test_GET_method(self):
        res = self.client.get(reverse('product:report-nation-made-in-equal'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'product/product-made-in-nation-report.html')
        self.assertEqual(len(res.context['products']), 1)
