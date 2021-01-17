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
        data = {
            'first_name': model.first_name,
            'last_name': model.last_name,
            'email': model.email,
            'password': model.password,
            'username': model.username
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
