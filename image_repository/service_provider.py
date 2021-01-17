from dependency_injector import containers, providers
from image_repository.repositories.ImageRepository import DjangoORMImageRepository, ImageRepository
from image_repository.services.ImageManagementService import DefaultImageManagementService, ImageManagementService
from image_repository.repositories.OwnerRepository import DjangoOwnerRepository, OwnerRepository
from image_repository.services.OwnerManagementService import DefaultOwnerManagementService, OwnerManagementService
from typing import Callable


class Container(containers.DynamicContainer):
    config = providers.Configuration()

    image_repository: Callable[[], ImageRepository] = providers.Factory(
        DjangoORMImageRepository
    )

    image_management_service: Callable[[], ImageManagementService] = providers.Factory(
        DefaultImageManagementService,
        repository=image_repository
    )

    owner_repository: Callable[[], OwnerRepository] = providers.Factory(
        DjangoOwnerRepository
    )
    owner_management_service: Callable[[], OwnerManagementService] = providers.Factory(
        DefaultOwnerManagementService,
        repository=owner_repository
    )


app_service_provider = Container()
