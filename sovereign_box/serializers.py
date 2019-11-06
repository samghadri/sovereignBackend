from rest_framework import serializers

from .models import Coins, CoinTag, ContactUs, CoinOffer

from django.conf import settings
import cloudinary

from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


def cloudinary_image_url(image, **kwargs):
    """
    Convenience function that returns a URL for an image from Cloudinary CDN
    with appropriate attributes.

    Allowed attributes:
    width
    height
    crop
    gravity
    radius
    effect
    """

    if image:
        kwargs["secure"] = True
        return cloudinary.CloudinaryImage(public_id=image.public_id, url_options=kwargs).url

    return None


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class AuthTokenserializer(serializers.Serializer):

    username = serializers.CharField()

    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):

        """ validate and authenticate user """
        username = attrs.get('username')

        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=username,
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

    image_url_2 = serializers.SerializerMethodField()

    def get_image_url(self, obj):
        if obj.image:
            return cloudinary_image_url(obj.image)

    def get_image_url_2(self, obj):
        if obj.image_2:
            return cloudinary_image_url(obj.image_2)

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


class CoinOfferSerializer(serializers.ModelSerializer):

    person = serializers.CharField(required=True)

    offer = serializers.CharField(required=True)

    coin = serializers.CharField(required=True)

    class Meta:
        model = CoinOffer
        fields = '__all__'
