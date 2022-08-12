from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from django.shortcuts import render
from .serializers import *
from .scripts import *
from .models import *

class LBViewSet(viewsets.ModelViewSet):
    """
    Generate leaderboard or submit a new solve attempt
    """
    def get(self, request, format=None):
        return JsonResponse(getLeaderboard())

    def post(self, request, format=None):
        """
        Checks submitted solution hash against the stored one for that assignment

                Parameters:
                        sol (str):      sha256 hash of submitted solution
                        team (str):     sha256 hash of team pass for submissions
                        event (str):    name associated with event being solved
                
                Side Effects:
                        If solution is accepted, flips solved bool to true on the assignment

                Returns:
                        Boolean for whether the solution was accepted
        """
        event_object = Event.objects.filter(name=request.POST.get("event"))
        team_object = Team.objects.filter(hash=hash(request.POST.get("team")))
        assignment_object = Assignment.objects.filter(event=event_object,team=team_object)
        event_hash_check = checkHash(hash(request.POST.get("sol")), event_object.hash)
        if event_hash_check: 
            assignment_object.update(solved=True)
            return JsonResponse({"solved":True})
        else:
            return JsonResponse({"solved":False})

class MemberViewSet(viewsets.ModelViewSet):
    """
    Retrieve public member info or create a new member
    """
    def get(self, request, format=None):
        """
        Returns list of members on the specified team

                Parameters in request:
                        t (str): Team name being requested

                Returns:
                        JSON formatted list of Member objects in that Team
        """
        return JsonResponse(getMemberList(request.GET.get("team")))

    def post(self, request, format=None):
        p_uname = request.POST.get("uname")
        p_is_owner = request.POST.get("is_owner")
        p_hash = hash(request.POST.get("hash"))
        p_email = request.POST.get("email")
        p_team = Team.objects.filter(name=request.POST.get("team"))
        new_member = Member.objects.create(
            uname = p_uname,
            is_owner = p_is_owner,
            hash = p_hash,
            email = p_email,
            team = p_team,
        )
        new_member.save()

class TeamViewSet(viewsets.ModelViewSet):
    """
    Retrieve team info or create a new team
    """
    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        p_name = request.POST.get("name")
        p_hash = hash(request.POST.get("hash"))
        new_team = Team.objects.create(
            name = p_name,
            hash = p_hash
        )
        new_team.save()
