from pyexpat import model
from django.db import models

class Puzzle(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField
    solution = models.CharField(max_length=64)
    riddle = models.CharField(max_length=512)
    url = models.URLField
    location = models.CharField(max_length=64)
    tags = models.CharField(max_length=256)

class Team(models.Model):
    name = models.CharField(max_length=26)
    hash = models.CharField(max_length=64)
    d0p = models.ForeignKey(Puzzle,
                            related_name='d1puzzle',
                            on_delete=models.CASCADE)
    d1p = models.ForeignKey(Puzzle,
                            related_name='d2puzzle',
                            on_delete=models.CASCADE)
    d2p = models.ForeignKey(Puzzle,
                            related_name='d3puzzle',
                            on_delete=models.CASCADE)
    d3p = models.ForeignKey(Puzzle,
                            related_name='d4puzzle',
                            on_delete=models.CASCADE)
    d4p = models.ForeignKey(Puzzle,
                            related_name='d5puzzle',
                            on_delete=models.CASCADE)
    d5p = models.ForeignKey(Puzzle,
                            related_name='d6puzzle',
                            on_delete=models.CASCADE)
    d6p = models.ForeignKey(Puzzle,
                            related_name='d7puzzle',
                            on_delete=models.CASCADE)
    d7p = models.ForeignKey(Puzzle,
                            related_name='d8puzzle',
                            on_delete=models.CASCADE)
    d8p = models.ForeignKey(Puzzle,
                            related_name='d9puzzle',
                            on_delete=models.CASCADE)
    d9p = models.ForeignKey(Puzzle,
                            related_name='d10puzzle',
                            on_delete=models.CASCADE)
    d0f = models.BooleanField
    d1f = models.BooleanField
    d2f = models.BooleanField
    d3f = models.BooleanField
    d4f = models.BooleanField
    d5f = models.BooleanField
    d6f = models.BooleanField
    d7f = models.BooleanField
    d8f = models.BooleanField
    d9f = models.BooleanField

class Member(models.Model):
    f_name = models.CharField(max_length=26)
    l_name = models.CharField(max_length=26)
    email = models.EmailField
    team = Team
    is_owner = models.BooleanField

class Solve(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    puzzle = models.OneToOneField(Puzzle, on_delete=models.CASCADE)
    timestamp = models.DateTimeField
    points = models.IntegerField
