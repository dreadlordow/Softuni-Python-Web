from django.urls import path

from petstagram.pets.views import list_pets, details_or_comment_pet, like_pet, create, edit_pet, delete_pet

urlpatterns =[
    path('', list_pets, name='list pets'),
    path('details/<int:pk>/', details_or_comment_pet, name='pet details'),
    path('like/<int:pk>/', like_pet, name='like pet'),
    path('create/', create, name='create pet'),
    path('edit/<int:pk>', edit_pet, name='edit pet'),
    path('delete/<int:pk>', delete_pet, name='delete pet'),
]