from django.urls import path

from django102 import views
from django102.views import index as index_view, UsersListView, GamesListView, something

urlpatterns = [
    path('', index_view, name='index'),
    path('2/', UsersListView.as_view()),
    path('games/', GamesListView.as_view()),
    path('smth/', something),
    path('create-game/', views.create_game)
]