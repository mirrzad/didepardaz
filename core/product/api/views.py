from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer, BrandSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter
from product.models import Brand, Product
from django.core.paginator import Paginator
from django.db.models import F


class BrandListApiView(APIView):
    """
    filter the list of brands based on the nationality parameter.
    this view is for demanded report number 1.

    params:
    GET: nationality, page, limit

    """

    serializer_class = BrandSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(name='nationality', location=OpenApiParameter.QUERY, description='nationality',
                             required=False, type=str),
            OpenApiParameter(name='page', location=OpenApiParameter.QUERY, description='page number',
                             required=False, type=int),
            OpenApiParameter(name='limit', location=OpenApiParameter.QUERY, description='limit number',
                             required=False, type=int),
        ],
    )
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


class ProductListApiView(APIView):
    """
     filter the list of products based on the brand parameter.
     filter the products with same brand nationality and manufacture if "nation_made_in_equal" parameter is given.
     this view is for demanded report number 2, 3.

     params:
     GET: page, limit, brand, nation_made_in_equal

    """

    serializer_class = ProductSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(name='brand', location=OpenApiParameter.QUERY, description='filter by brand',
                             required=False, type=str),
            OpenApiParameter(name='page', location=OpenApiParameter.QUERY, description='page number',
                             required=False, type=int),
            OpenApiParameter(name='limit', location=OpenApiParameter.QUERY, description='limit number',
                             required=False, type=int),
            OpenApiParameter(name='nation_made_in_equal', location=OpenApiParameter.QUERY,
                             description='fill this parameter if you want to '
                                         'filter products with same nation and manufacture',
                             required=False, type=int),
        ],
    )
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
