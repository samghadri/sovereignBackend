from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CoinsSerializer
from .models import Coins

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


class CoinParams(object):
    def __init__(self, data):
        self.limit = data.get("limit", 5)
        self.offset = data.get("offset", 0)
        self.metal_type = data.get("metal_type")
        self.tags = data.get("tags")
        self.tags_list = self._parse_list(self.tags)

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

        queryset = queryset.all()[params.offset:params.offset + params.limit]

        serializer = CoinsSerializer(queryset, many=True)

        result_data = serializer.data

        result = {
            "result": result_data
        }

        return Response(result)
