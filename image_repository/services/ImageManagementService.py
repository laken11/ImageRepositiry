from image_repository.repositories.ImageRepository import ImageRepository
from typing import List, Dict
from abc import abstractmethod, ABCMeta
from image_repository.Dto.ImageDto import *


class ImageManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_image(self,  model: CreateImageDto):
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


class DefaultImageManagementService(ImageManagementService):
    repository: ImageRepository

    def __init__(self, repository: ImageRepository):
        self.repository = repository

    def create_image(self,  model: CreateImageDto):
        return self.repository.create_image(model)

    def edit_image(self, image_id: int, model: EditImageDto):
        return self.repository.edit_image(image_id, model)

    def list_image(self) -> List[ListImageDto]:
        return self.repository.list_image()

    def search_image(self, tag: str):
        return self.repository.search_image(tag)

    def image_details(self, name: str) -> ImageDetailsDto:
        return self.repository.image_details(name)

    def delete_image(self, image_id):
        return self.repository.delete_image(image_id)

    def get_image_by_id(self, image_id):
        return self.repository.get_image_by_id(image_id)
