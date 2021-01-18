from django.contrib.auth.models import User

from image_repository.Dto.OwnerDto import *
from abc import ABCMeta, abstractmethod

from image_repository.serilizer import OwnerSerializer


class OwnerRepository(metaclass=ABCMeta):
    @abstractmethod
    def register_owner(self, model: RegisterOwnerDto):
        """Register Owner Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_owner(self, owner_id, model: EditOwnerDto):
        """Edit Owner Object"""
        raise NotImplementedError


class DjangoOwnerRepository(OwnerRepository):
    def register_owner(self, model: RegisterOwnerDto):
        errors = []
        user = User.objects.create_user(username=model.username, email=model.email, password=model.password)
        user.first_name = model.first_name
        user.last_name = model.last_name
        user_id = user.id
        data = {
            'user_id': user_id,
            'info': model.owner_info
        }
        serializer = OwnerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            errors.append(serializer.errors)
        return errors

    def edit_owner(self, owner_id, model: EditOwnerDto):
        errors = []
        data = {
            'first_name': model.first_name,
            'last_name': model.last_name,
            'email': model.email,
            'username': model.username
        }
        serializer = OwnerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            errors.append(serializer.errors)
        return errors
