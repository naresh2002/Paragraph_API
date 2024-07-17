from rest_framework import serializers
from .models import CustomUser, Paragraph, Word

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'email', 'dob', 'password', 'created_at', 'modified_at']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = '__all__'

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'
