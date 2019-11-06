from rest_framework import serializers

from .models import Coins, CoinTag, ContactUs

from django.conf import settings

from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name', 'password', 'email')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class AuthTokenserializer(serializers.Serializer):

    email = serializers.CharField()

    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):

        """ validate and authenticate user """
        email = attrs.get('email')

        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )

        if not user:
            msg = _('unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs


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

    email_address = serializers.CharField(required=True)

    description = serializers.CharField(required=True)

    class Meta:
        model = ContactUs
        fields = '__all__'
