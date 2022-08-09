from rest_framework import serializers
from .models import Puzzle, Team, Member, Solve

# TODO: update serializers to use dynamic fields for optional model fields

class TeamPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('name','hash')

class MemberPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ('uname', 'email', 'team', 'is_team_owner')

class SolvePostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Solve
        fields = ('team', 'puzzle', 'points')
