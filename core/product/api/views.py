from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer, BrandSerializer
from product.models import Brand, Product
from django.core.paginator import Paginator
from django.db.models import F


class ProductListApiView(APIView):
    serializer_class = ProductSerializer

    def get(self, request):
        brand = request.query_params.get('brand', None)
        nation_made_in_equal = request.query_params.get('nation_made_in_equal', None)
        if brand:
            products = Product.objects.filter(brand__title__iexact=brand)
            if not products:
                return Response({'details': 'This brand does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            if nation_made_in_equal:
                products = Product.objects.filter(made_in=F('brand__nationality'))
            else:
                products = Product.objects.all()
        page_num = request.query_params.get('page', 1)
        limit = request.query_params.get('limit', 5)
        paginator = Paginator(products, limit)
        try:
            srz_data = self.serializer_class(instance=paginator.page(page_num), many=True)
        except:
            return Response({'detail': 'This page contains no results'}, status=status.HTTP_404_NOT_FOUND)
        return Response(srz_data.data, status=status.HTTP_200_OK)


class BrandListApiView(APIView):
    serializer_class = BrandSerializer

    def get(self, request):
        nationality = request.query_params.get('nationality', None)
        if nationality:
            brands = Brand.objects.filter(nationality__iexact=nationality)
        else:
            brands = Brand.objects.all()
        page_num = request.query_params.get('page', 1)
        limit = request.query_params.get('limit', 5)
        paginator = Paginator(brands, limit)
        try:
            srz_data = self.serializer_class(instance=paginator.page(page_num), many=True)
        except:
            return Response({'detail': 'This page contains no results'}, status=status.HTTP_404_NOT_FOUND)
        return Response(srz_data.data, status=status.HTTP_200_OK)
