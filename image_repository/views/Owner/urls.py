from django.urls import path
from image_repository.views.Owner import view


urlpatterns = [
    path('owner', view.owner),
    path('edit_owner/<int:owner_id>', view.edit_owner)
]
