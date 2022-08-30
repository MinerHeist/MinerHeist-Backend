from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

from django.shortcuts import render
from .serializers import *
from .scripts import *
from .models import *

@csrf_exempt
def LBView(request):
    """
    Generate leaderboard or submit a new solve attempt
    """
    if request.method == 'GET':
        return JsonResponse(getLeaderboard())

    if request.method == 'POST':
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
        event_object = Event.objects.get(name=request.POST.get("event"))
        team_object = Team.objects.get(hash=hash(request.POST.get("team")))
        assignment_object = Assignment.objects.get(event=event_object,team=team_object)
        event_hash_check = checkHash(hash(request.POST.get("sol")), event_object.solution)
        if event_hash_check: 
            assignment_object.solved=True
            assignment_object.save()
            return JsonResponse({"solved":True})
        else:
            return JsonResponse({"solved":False})

@csrf_exempt
def MemberView(request):
    """
    Retrieve public member info or create a new member
    """

    if request.method == 'GET':
        """
        Returns list of members on the specified team

                Parameters in request:
                        t (str): Team name being requested

                Returns:
                        JSON formatted list of Member objects in that Team
        """
        return JsonResponse(getMemberList(request.GET.get("team")))

    if request.method == 'POST':
        p_uname = request.POST.get("uname")
        p_is_owner = request.POST.get("is_owner")
        p_hash = hash(request.POST.get("hash"))
        p_email = request.POST.get("email")
        p_team = Team.objects.get(name=request.POST.get("team"))
        new_member = Member.objects.create(
            uname = p_uname,
            is_owner = p_is_owner,
            hash = p_hash,
            email = p_email,
            team = p_team,
        )
        new_member.save()
        return HttpResponse("successfully added member")

@csrf_exempt
def TeamView(request):
    """
    Retrieve team info or create a new team
    """
    if request.method == 'GET':
        return JsonResponse(getTeamList())

    if request.method == 'POST':
        p_name = request.POST["name"]
        p_hash = hash(request.POST["hash"])
        new_team = Team.objects.create(
            name = p_name,
            hash = p_hash
        )
        new_team.save()
        return HttpResponse("successfully created team")
