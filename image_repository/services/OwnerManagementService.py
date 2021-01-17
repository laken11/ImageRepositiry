from image_repository.repositories.OwnerRepository import OwnerRepository
from abc import ABCMeta, abstractmethod
from image_repository.Dto.OwnerDto import *


class OwnerManagementService(metaclass=ABCMeta):
    @abstractmethod
    def register_owner(self, model: RegisterOwnerDto):
        """Register Owner Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_owner(self, owner_id, model: EditOwnerDto):
        """Edit Owner Object"""
        raise NotImplementedError


class DefaultOwnerManagementService(OwnerManagementService):
    repository: OwnerRepository

    def __init__(self, repository: OwnerRepository):
        self.repository = repository

    def register_owner(self, model: RegisterOwnerDto):
        return self.repository.register_owner(model)

    def edit_owner(self, owner_id, model: EditOwnerDto):
        return self.repository.edit_owner(owner_id, model)
