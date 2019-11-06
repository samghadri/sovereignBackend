from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q

from .serializers import CoinsSerializer, CoinTagSerializer, ContactUsSerializer, UserSerializer, AuthTokenserializer
from .models import Coins, CoinTag

from rest_framework.serializers import Serializer
from rest_framework.fields import CharField, IntegerField
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .permissions import RequiresAuthenticationMixin


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


class CoinsListView(RequiresAuthenticationMixin, APIView):
    def get(self, request):
        # permission_classes = [IsAuthenticated]
        # above we are not using this as we are
        # working with requires authenticationMixin
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

            term_filter = Q(name__icontains=params.search_text) | Q(description__icontains=params.search_text)

            queryset = queryset.filter(term_filter)

        count = queryset.count()

        queryset = queryset.all()[params.offset:params.offset + params.limit]

        serializer = CoinsSerializer(queryset, many=True)

        result_data = serializer.data

        result = {
            "result": result_data,
            "count": count,
        }
        print("this is request", request)

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


class ContactUsView(APIView):

    def post(self, request):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateUserView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateTokenView(ObtainAuthToken):
    serializes_classs = AuthTokenserializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
