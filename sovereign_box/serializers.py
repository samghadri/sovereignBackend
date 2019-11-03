from rest_framework import serializers

from .models import Coins, CoinTag, ContactUs

from django.conf import settings


class CoinTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoinTag
        fields = '__all__'


class CoinsSerializer(serializers.ModelSerializer):

    tags = CoinTagSerializer(many=True)

    image_url = serializers.SerializerMethodField()

    def get_image_url(self, obj):
        if obj.image:
            full_url = settings.BACKEND_URL + obj.image.url
            return full_url

    class Meta:
        model = Coins
        exclude = ('image',)


class ContactUsSerializer(serializers.ModelSerializer):

    full_name = serializers.CharField(required=True)

    email = serializers.CharField(required=True)

    description = serializers.CharField(required=True)

    class Meta:
        model = ContactUs
        fields = '__all__'
