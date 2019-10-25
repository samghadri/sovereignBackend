from rest_framework import serializers

from .models import Coins, CoinTag


class CoinTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoinTag
        fields = '__all__'


class CoinsSerializer(serializers.ModelSerializer):

    tags = CoinTagSerializer(many=True)

    class Meta:
        model = Coins
        fields = '__all__'
