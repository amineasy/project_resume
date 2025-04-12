from rest_framework import serializers

from project_resume.apps.accounts.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'confirm_password']

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("رمز عبور و تایید رمز عبور باید یکسان باشند.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = CustomUser.objects.create(**validated_data)
        return user











class PasswordRestSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)




class VerifyCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=5)



class NewPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(min_length=6, write_only=True)
    confirm_password = serializers.CharField(min_length=6, write_only=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("رمزها با هم مطابقت ندارند.")
        return data













