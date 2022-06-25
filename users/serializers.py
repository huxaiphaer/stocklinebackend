from django.contrib.auth import authenticate
from rest_framework import serializers

from users.models import User


class TokenObtainPairResponseSerializer(serializers.Serializer):
    """Token serializer generator."""

    access = serializers.CharField()
    refresh = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer to register a user.
    """
    tokens = TokenObtainPairResponseSerializer(read_only=True)
    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'tokens', 'password', 'uuid',)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    """
    Login Serializer Class.
    """

    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    tokens = TokenObtainPairResponseSerializer(read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User

    def validate(self, data):
        """
        Validate the data from the post request within serializer.

        :data: Data for the Login data

        :return: An an object of user after login.
        """
        user = authenticate(email=data.get('email'),
                            password=data.get('password'))

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.')

        # Django provides a flag on our `User` model called `is_active`. The
        # purpose of this flag to tell us whether the user has been banned
        # or otherwise deactivated.
        if not user.is_active:
            raise serializers.ValidationError('This user has been deactivated.')

        return {
            'tokens': user.tokens,
            'email': user.email,
            'username': user.username,
            'uuid': user.uuid,
            'id': user.id,
        }

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

