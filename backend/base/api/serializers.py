# from rest_framework.serializers import ModelSerializer
# from base.models import Note


# class NoteSerializer(ModelSerializer):
#     class Meta:
#         model = Note
#         fields = '__all__'



from rest_framework.serializers import ModelSerializer
# from base.models import Product
from django.contrib.auth.models import User 
from rest_framework import serializers

# -----------------------------------------


# class NoteSerializer(ModelSerializer):
#     class Meta:
#         model = Note
#         fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user



class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


# ------------------------------------------------------------------

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'price')
