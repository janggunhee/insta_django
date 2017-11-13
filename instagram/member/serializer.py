from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'img_profile',
            'age',
        )

class SignupSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'pk'
            'username',
            'img_profile',
            'password1',
            'password2',
            'age',
            'token',
        )

        def validate(self, data):
            if data['password1'] != ['password2']:
                raise serializers.ValidationError('비밀번호 불일치')
            return data

        def create(self, validated_data):
            return User.objects.create_user(
                username=validated_data['username'],
                password=validated_data['password'],
            )
        @staticmethod
        def get_token(obj):
            # token, token_create = Token.objects.get_or_create(user=obj)
            # return token.key
            return Token.objects.create(user=obj)[0].key

