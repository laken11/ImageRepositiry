from django.contrib.auth.models import User
from rest_framework import serializers
from image_repository.models import Owner, Image


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=None)
    last_name = serializers.CharField(max_length=None)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, max_length=None)
    username = serializers.CharField(max_length=None)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass


class OwnerSerializer(serializers.Serializer):
    user = UserSerializer(many=False, read_only=True)
    info = serializers.CharField(max_length=500)
    user_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        return Owner.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass


class ImageSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    tag = serializers.CharField(max_length=20, default=name)
    tag2 = serializers.CharField(max_length=20, allow_null=True, allow_blank=True, required=False)
    tag3 = serializers.CharField(max_length=20, allow_null=True, allow_blank=True, required=False)
    description = serializers.CharField(max_length=500)
    image = serializers.ImageField(use_url=True)
    owner_id = serializers.IntegerField(write_only=True)
    owner_info = serializers.CharField(max_length=500, read_only=True)
    user = UserSerializer(many=False, read_only=True)

    def create(self, validated_data):
        return Image.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.tag = validated_data.get('tag', instance.tag)
        instance.tag2 = validated_data.get('tag2', instance.tag2)
        instance.tag3 = validated_data.get('tag3', instance.tag3)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.owner_id = validated_data.get('owner_id', instance.owner_id)
        instance.save()
        return instance



