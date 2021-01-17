from abc import ABCMeta, abstractmethod
from typing import List

from django.contrib.auth.models import User
from django.db.models import Q
from image_repository.Dto.ImageDto import ImageDetailsDto, CreateImageDto, EditImageDto, ListImageDto
from image_repository.models import Image, Owner
from image_repository.serilizer import ImageSerializer


class ImageRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_image(self, model: CreateImageDto):
        """Create Image Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_image(self, image_id: int, model: EditImageDto):
        """Edit Image Object"""
        raise NotImplementedError

    @abstractmethod
    def list_image(self) -> List[ListImageDto]:
        """List Image Objects"""
        raise NotImplementedError

    @abstractmethod
    def image_details(self, name: str) -> ImageDetailsDto:
        """Return Image Details Object"""
        raise NotImplementedError

    @abstractmethod
    def search_image(self, tag: str):
        """Return Similar Image Objects"""
        raise NotImplementedError

    @abstractmethod
    def delete_image(self, image_id):
        """Delete Image Object"""
        raise NotImplementedError

    @abstractmethod
    def get_image_by_id(self, image_id):
        """Return Image Object"""
        raise NotImplementedError


class DjangoORMImageRepository(ImageRepository):
    def create_image(self, model: CreateImageDto):
        error = []
        data = {
            'name': model.name,
            'tag': model.tag,
            'tag2': model.tag2,
            'tag3': model.tag3,
            'image': model.image,
            'description': model.description,
            'owner_id': model.owner_id
        }
        serializer = ImageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            error.append(serializer.errors)
        return error

    def list_image(self) -> List[ListImageDto]:
        images = Image.objects.all()
        result: List[ListImageDto] = []
        for image in images:
            item = ListImageDto()
            item.tag = image.tag
            item.tag3 = image.tag3
            item.tag2 = image.tag2
            item.name = image.name
            item.image = image.image
            item.description = image.description
            owner_id = image.owner_id
            owner = Owner.objects.get(id=owner_id)
            user_id = owner.user_id
            user = User.objects.get(id=user_id)
            item.owner_info = owner.info
            item.user = user
            result.append(item)
        return result

    def edit_image(self, image_id: int, model: EditImageDto):
        try:
            image = Image.objects.get(id=image_id)
            data = {
                'name': model.name,
                'tag2': model.tag2,
                'image': model.image,
                'tag3': model.tag3,
                'tag': model.tag,
                'description': model.description
            }
            serializer = ImageSerializer(image, data=data)
            if serializer.is_valid():
                serializer.save()
                return True
            else:
                return serializer.errors
        except Image.DoesNotExist as e:
            raise e

    def image_details(self, name: str) -> ImageDetailsDto:
        try:
            image = Image.objects.get(name=name)
            result = ImageDetailsDto()
            result.image = image.image
            result.tag = image.tag
            result.tag2 = image.tag2
            result.tag3 = image.tag3
            result.description = image.description
            result.name = image.name
            owner_id = image.owner_id
            owner = Owner.objects.get(id=owner_id)
            result.owner_info = owner.info
            user_id = owner.user_id
            user = User.objects.get(id=user_id)
            result.user = user
            return result
        except Image.DoesNotExist as e:
            raise e

    def search_image(self, tag: str):
        try:
            images = Image.objects.filter(
                Q(tag__contains=tag) | Q(tag2__contains=tag) | Q(
                    tag3__contains=tag))
            result: List[ListImageDto] = []
            for image in images:
                item = ListImageDto()
                item.tag = image.tag
                item.tag2 = image.tag2
                item.tag3 = image.tag3
                item.name = image.name
                item.image = image.image
                item.description = image.description
                owner_id = image.owner_id
                owner = Owner.objects.get(id=owner_id)
                item.owner_info = owner.info
                user_id = owner.user_id
                user = User.objects.get(id=user_id)
                item.user = user
                result.append(item)
            return result
        except Image.DoesNotExist as e:
            raise e

    def delete_image(self, image_id):
        try:
            image = Image.objects.get(id=image_id)
            image.delete()
            return True
        except Image.DoesNotExist as e:
            raise e

    def get_image_by_id(self, image_id):
        try:
            image = Image.objects.get(id=image_id)
            result = ImageDetailsDto()
            result.owner_id = image.owner_id
            return result
        except Exception as e:
            raise e
