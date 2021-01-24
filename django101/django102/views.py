from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from django102.models.game import Game
from django102.models.game2 import Game2
from django102.models.person import Person
from django102.models.player import Player


def something(request):
    return HttpResponse("<u>It works!</u>")


def index(request):
    title = 'SoftUni Django 101'
    users = User.objects.all()
    games = Game2.objects.all()

    context = {
        'title': title,
        'users': users,
        'games': games,
        # 'users': [],
    }

    return render(request, 'index.html', context)


class UsersListView(ListView):
    model = User
    template_name = 'index2.html'
    queryset = User.objects.all().order_by('-username')

    def get_context_object_name(self, object_list):
        return 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'From class view'
        return context


class GamesListView(ListView):
    model = Game
    template_name = 'games.html'


def create_game(request):
    game = Game2(
        game_name='lEAGUE',
        level=Game2.EASY,
    )
    game.save()
    return redirect(request, 'index')