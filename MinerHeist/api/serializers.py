from rest_framework import serializers
from .models import Event, Team, Member, Assignment

# TODO: update serializers to use dynamic fields for optional model fields

class TeamPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = (
            'name',
            'hash',
        )

class MemberPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = (
            'uname',
            'email',
            'team',
            'is_owner',
            'hash',
        )

class EventPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = (
            'name',
            's_date',
            'e_date',
            'points',
            'solution',
            'hint',
            'tags',
            'location',
            'url_slug',
        )

class AssignmentPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assignment
        fields = (
            'event',
            'index',
            's_time',
            'team',
            'solved',
            'member',
            's_member',
            'found',
        )
