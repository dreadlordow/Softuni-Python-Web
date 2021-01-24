from django.db import models

from django102.models.player import Player


class Game2(models.Model):
    EASY = 1
    MEDIUM = 2
    HARD = 3
    DIFFICULTY_LEVELS_CHOICES = (
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard'),
    )
    game_name = models.CharField(max_length=20)
    level = models.CharField(max_length=2,default=0, choices=DIFFICULTY_LEVELS_CHOICES)
    players = models.ManyToManyField(Player)


