from django.shortcuts import render, redirect
from django.views import View
from .forms import AddBrandForm, AddProductForm, BrandFilterForm
from .models import Brand, Product
from django.contrib import messages
from django.db.models import F


class IndexView(View):
    """
    Index Page for the product app.
    """
    template_name = 'product/index.html'

    def get(self, request):
        return render(request, self.template_name)


class AddBrandView(View):
    """
    Creates brand objects in model:product.Brand

    methods:
    GET: serve a ModelForm for model:product.Brand
    POST: create a brand object after validation
    """
    template_name = 'product/add-brand.html'
    form_class = AddBrandForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            Brand.objects.create(**form.cleaned_data)
            messages.success(request, 'Brand added successfully.', 'success')
            return redirect('product:add-brand')
        return render(request, self.template_name, {'form': form})


class AddProductView(View):
    """
    Creates product objects in model:product.Product

    methods:
    GET: serve a ModelForm for model:product.Product
    POST: create a product object after validation
    """
    template_name = 'product/add-product.html'
    form_class = AddProductForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            messages.success(request, 'Product added successfully.', 'success')
            return redirect('product:add-product')
        return render(request, self.template_name, {'form': form})


class BrandReport(View):
    """
    filter the list of brands based on the korean nationality.
    this view is for demanded report number 1.
    """

    template_name = 'product/brand-report.html'

    def get(self, request):
        brands = Brand.objects.filter(nationality__iexact='korea')
        return render(request, self.template_name, {'brands': brands})


class ProductReport(View):
    """
    filter the list of products based on the brand parameter.
    this view is for demanded report number 2.

    params:
    GET: brand
    """
    template_name = 'product/product-report.html'
    form_class = BrandFilterForm

    def get(self, request):
        products = Product.objects.all()
        if request.GET.get('brand', None):
            products = products.filter(brand__id=request.GET['brand'])
            return render(request, self.template_name, {'products': products, 'form': self.form_class})
        return render(request, self.template_name, {'products': products, 'form': self.form_class})


class ProductMadeInNationEqualReport(View):
    """
    filter the list of products with same brand nationality and manufacture.
    this view is for demanded report number 3.
    """

    template_name = 'product/product-made-in-nation-report.html'

    def get(self, request):
        products = Product.objects.filter(made_in=F('brand__nationality'))
        return render(request, self.template_name, {'products': products})


class A:
    """fix bug2 test test
        test7878   213123123132132132121
    """
    pass

