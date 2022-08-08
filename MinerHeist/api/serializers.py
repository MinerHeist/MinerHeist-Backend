from rest_framework import serializers
from .models import Puzzle, Team, Member, Solve

class TeamPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('name','hash','owner')

class TeamGetSerializer(serializers.HyperlinkedModelSerializer):
    pass

class MemberPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ('uname', 'email', 'team', 'is_team_owner')

class SolvePostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Solve
        fields = ('team', 'puzzle', 'points')

class SolveGetSerializer(serializers.HyperlinkedModelSerializer):
    pass