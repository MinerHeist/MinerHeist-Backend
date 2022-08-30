from ast import Assign
from pyexpat import model
from re import L
from django.db import models

class Event(models.Model):
    """
    Stores metadata for and a URL slug to and individual Event

        Fields:
            name    (str):      Name for the event
            s_date  (Date):     Start date of event
            e_date  (Date):     End date of event
            points  (int):      How many points completion is worth
            solution(str):      sha256 hash of the solution to the event
            hint    (str):      Help or prompt to locate event, optional
            tags    (str):      Comma separated event descriptors, optional
            location(str):      sha256 hash of the location of the event, optional
            url_slug(Slug):     Slug to append to Event URL to access the event
    """
    name = models.CharField(max_length=50, unique=True)
    s_date = models.DateTimeField(blank=True, null=True)
    e_date = models.DateTimeField(blank=True, null=True)
    points = models.IntegerField(default=100)
    solution = models.CharField(max_length=64)
    hint = models.CharField(max_length=512, blank=True)
    tags = models.CharField(max_length=256, blank=True)
    location = models.CharField(max_length=64, blank=True)
    url_slug = models.SlugField(max_length=64, default="default-slug", blank=True, unique=True)

class Team(models.Model):
    """
    Stores name and password hash for a Team, optionally the URL to a logo image

        Fields:
            name    (str):      Name for the team
            hash    (str):      Password hash for authenticating solves/invites
            avatar  (URL):      Link to avatar image, optional
            points  (int):      Computed value that generates current score
    """
    name = models.CharField(max_length=26, unique=True)
    hash = models.CharField(max_length=64, unique=True)
    avatar = models.URLField(max_length=200, blank=True)
    
    @property
    def points(self) -> int:
        total = 0
        for a in Assignment.objects.filter(team=self):
            if a.solved:
                total += a.event.points
        return total

class Member(models.Model):
    """
    Stores username, email, team membership, and ownership status for a Member

        Fields:
            uname   (str):      User specified username
            is_owner(bool):     Does the user own their Team
            hash    (str):      sha256 hash of password, optional
            avatar  (URL):      Link to avatar image, optional
            email   (Email):    Contact info for Member, optional
            team    (Team):     Team the user belongs to
    """
    uname = models.CharField(max_length=26, unique=True)
    is_owner = models.BooleanField(default=False)
    hash = models.CharField(max_length=64, blank=True, unique=True)
    avatar = models.URLField(max_length=200, blank=True)
    email = models.EmailField(max_length=256, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True)

class Assignment(models.Model):
    """
    Stores Event assignments for teams based on an index, including whether it has been found

        Fields:
            event   (Event):    The event being assigned
            index   (int):      Allows events to be ordinal, optional
            s_time  (DateTime): Timestamp for completion, optional
            team    (Team):     Can be assigned to a Team or null, optional
            solved  (Bool):     Has the event been completed yet
            member  (Member):   Can be assigned to individual Member, optional
            s_member(Member):   Can keep track of solving member of Team, optional
            found   (Bool):     Has the event been located yet, optional
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    index = models.IntegerField(default=0)
    s_time = models.DateTimeField(blank=True, null=True, default="")
    team = models.ForeignKey(Team, blank=True, null=True, on_delete=models.CASCADE)
    solved = models.BooleanField(default=False)
    member = models.ForeignKey(Member, blank=True, null=True, on_delete=models.CASCADE, related_name="assignedMember")
    s_member = models.ForeignKey(Member, blank=True, null=True, on_delete=models.CASCADE, related_name="solvingMember")
    found = models.BooleanField(default=False, blank=True)

    