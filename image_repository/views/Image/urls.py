from django.urls import path
from image_repository.views.Image import view


urlpatterns = [
    path('image/', view.image),
    path('image_details/<int:image_id>', view.image_details),
    path('search/<str:tag>', view.search_image),
    path('create_image/', view.create_image),
    path('get_image/<str:name>', view.get_image)
]
