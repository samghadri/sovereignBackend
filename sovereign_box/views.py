from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Q

from .serializers import CoinsSerializer, CoinTagSerializer
from .models import Coins, CoinTag

from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework.fields import CharField, BooleanField, IntegerField, SerializerMethodField


class ParamsSerializer(Serializer):
    """
    Validates parameters for search
    """
    limit = IntegerField(required=False)
    offset = IntegerField(required=False)
    tags = CharField(required=False)
    metal_type = CharField(required=False)
    searchText = CharField(required=False)


class CoinParams(object):
    def __init__(self, data):
        self.limit = data.get("limit", 2)
        self.offset = data.get("offset", 0)
        self.metal_type = data.get("metal_type")
        self.tags = data.get("tags")
        self.tags_list = self._parse_list(self.tags)
        self.search_text = data.get("searchText")

    def _parse_list(self, txt, delimiter="|"):
        if txt:
            # support multiple tags by accepting pipe-delimited tags list
            return list(filter(None, txt.split(delimiter)))

        return []


class CoinsListView(APIView):

    def get(self, request):

        param_serializer = ParamsSerializer(data=request.query_params)

        if not param_serializer.is_valid():
            return Response(data=param_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        params = CoinParams(param_serializer.data)

        queryset = Coins.objects.distinct()

        if params.metal_type:
            queryset = queryset.filter(metal_type=params.metal_type)

        if params.tags_list:

            queryset = queryset.filter(tags__name__in=params.tags_list)

        if params.search_text:

            term_filter = Q(name__icontains=params.search_text)

            queryset = queryset.filter(term_filter)

        count = queryset.count()

        queryset = queryset.all()[params.offset:params.offset + params.limit]

        serializer = CoinsSerializer(queryset, many=True)

        result_data = serializer.data

        result = {
            "result": result_data,
            "count": count,
        }

        return Response(result)


class TagCoinView(APIView):

    def get(self, request):
        queryset = CoinTag.objects.all()
        serializer = CoinTagSerializer(queryset, many=True)
        result_data = serializer.data
        result = {
            "result": result_data
        }

        return Response(result)
