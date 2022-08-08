from pyexpat import model
from re import L
from django.db import models

class Puzzle(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField(default=100)
    solution = models.CharField(max_length=64)
    riddle = models.CharField(max_length=512)
    url = models.URLField(max_length=256, default='fixme.com')
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
    d0f = models.BooleanField(default=False)
    d1f = models.BooleanField(default=False)
    d2f = models.BooleanField(default=False)
    d3f = models.BooleanField(default=False)
    d4f = models.BooleanField(default=False)
    d5f = models.BooleanField(default=False)
    d6f = models.BooleanField(default=False)
    d7f = models.BooleanField(default=False)
    d8f = models.BooleanField(default=False)
    d9f = models.BooleanField(default=False)

class Member(models.Model):
    uname = models.CharField(max_length=26)
    email = models.EmailField(max_length=256, default='fixme@change.com')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    is_team_owner = models.BooleanField(default=False)

class Solve(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    puzzle = models.OneToOneField(Puzzle, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    points = models.IntegerField(default=100)
