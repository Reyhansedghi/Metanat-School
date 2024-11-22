from rest_framework import serializers
from account.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['phone_number', 'first_name', 'last_name', 'password1', 'password2']
    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            phone_number=validated_data['phone_number'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password1']
            #validated data is validate function output
        )
        return user
    

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'first_name', 'last_name', 'password', 'age','email']