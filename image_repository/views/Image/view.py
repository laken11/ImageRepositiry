from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from image_repository.Dto.ImageDto import *
from image_repository.service_provider import app_service_provider
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.status import *
from image_repository.serilizer import ImageSerializer


@api_view(['GET'])
def image(request):
    if request.method == 'GET':
        images = app_service_provider.image_management_service().list_image()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


@api_view(['POST'])
@csrf_exempt
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_image(request):
    if request.method == 'POST':
        images = __get_attribute_from_request(request)
        images.owner_id = request.user.owner.id
        serializer = app_service_provider.image_management_service().create_image(images)
        if not serializer:
            return Response(status=HTTP_200_OK)
        else:
            return Response(serializer, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def search_image(request, tag: str):
    if request.method == 'GET':
        images = app_service_provider.image_management_service().search_image(tag)
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_image(request, name: str):
    if request.method == 'GET':
        try:
            img = app_service_provider.image_management_service().image_details(name)
            serializer = ImageSerializer(img, many=False)
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception:
            raise NotFound


@api_view(['PUT', 'DELETE'])
@csrf_exempt
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def image_details(request, image_id):
    if request.method == 'PUT':
        owner_id = app_service_provider.image_management_service().get_image_by_id(image_id)
        if request.user.owner.id == owner_id.owner_id:
            try:
                img = __get_attribute_from_request_edit(request)
                img.owner_id = owner_id
                serializer = app_service_provider.image_management_service().edit_image(image_id, img)
                if serializer is True:
                    return Response(status=HTTP_200_OK)
                else:
                    return Response(status=HTTP_400_BAD_REQUEST)
            except Exception:
                raise AttributeError
        else:
            return Response(status=HTTP_401_UNAUTHORIZED)

    elif request.method == 'DELETE':
        owner_id = app_service_provider.image_management_service().get_image_by_id(image_id)
        if request.user.owner.id == owner_id.owner_id:
            try:
                stat = app_service_provider.image_management_service().delete_image(image_id)
                if stat is True:
                    return Response(status=HTTP_200_OK)
                else:
                    return Response(status=HTTP_400_BAD_REQUEST)
            except Exception:
                raise AttributeError
        else:
            return Response(status=HTTP_401_UNAUTHORIZED)


def __get_attribute_from_request(request):
    create_image_dto = CreateImageDto()
    create_image_dto.image = request.data['image']
    __set_attribute_from_request(request, create_image_dto)
    return create_image_dto


def __set_attribute_from_request(request, create_image_dto):
    create_image_dto.tag = request.data['tag']
    create_image_dto.tag2 = request.data.get('tag2', '')
    create_image_dto.tag3 = request.data.get('tag3', '')
    create_image_dto.description = request.data['description']
    create_image_dto.name = request.data['name']


def __get_attribute_from_request_edit(request):
    edit_image_dto = EditImageDto()
    edit_image_dto.image = request.data.get('image', '')
    __set_attribute_from_request_edit(request, edit_image_dto)
    return edit_image_dto


def __set_attribute_from_request_edit(request, edit_image_dto):
    edit_image_dto.tag3 = request.data.get('tag3', '')
    edit_image_dto.tag2 = request.data.get('tag2', '')
    edit_image_dto.tag = request.data.get('tag', '')
    edit_image_dto.name = request.data.get('name', '')
    edit_image_dto.description = request.data.get('description', '')
