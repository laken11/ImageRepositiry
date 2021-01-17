from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from image_repository.Dto.OwnerDto import *
from image_repository.service_provider import app_service_provider
from rest_framework.decorators import api_view
from rest_framework.status import *


@api_view(['POST'])
@csrf_exempt
def owner(request):
    if request.method == 'POST':
        image_owner = __get_attribute_from_request(request)
        if image_owner.password == image_owner.password:
            owner = app_service_provider.owner_management_service().register_owner(image_owner)
            if owner is []:
                return Response(status=HTTP_200_OK)
            else:
                return Response(owner, status=HTTP_400_BAD_REQUEST)
        else:
            return HttpResponse('Password dose Not Match')


@api_view(['PUT'])
def edit_owner(request, owner_id):
    if request.method == 'PUT':
        img = __get_attribute_from_request_edit(request)
        edit_owner_dto = app_service_provider.owner_management_service().edit_owner(owner_id, img)
        if edit_owner_dto is []:
            return Response(status=HTTP_200_OK)
        else:
            return Response(edit_owner_dto, status=HTTP_400_BAD_REQUEST)


def __get_attribute_from_request(request):
    register_owner_dto = RegisterOwnerDto()
    register_owner_dto.username = request.data['username']
    __set_attribute_from_request(request, register_owner_dto)
    return register_owner_dto


def __set_attribute_from_request(request, register_owner_dto):
    register_owner_dto.email = request.data['email']
    register_owner_dto.last_name = request.data['last_name']
    register_owner_dto.first_name = request.data['first_name']
    register_owner_dto.password = request.data['password']
    register_owner_dto.confirm_password = request.data['confirm_password']

def __get_attribute_from_request_edit(request):
    edit_owner_dto = EditOwnerDto()
    edit_owner_dto.username = request.data['username']
    __set_attribute_from_request_edit(request, edit_owner_dto)
    return edit_owner_dto


def __set_attribute_from_request_edit(request, edit_owner_dto):
    edit_owner_dto.email = request.data['email']
    edit_owner_dto.last_name = request.data['last_name']
    edit_owner_dto.first_name = request.data['first_name']
