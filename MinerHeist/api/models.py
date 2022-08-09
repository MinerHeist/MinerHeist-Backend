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
    name = models.CharField(max_length=50)
    s_date = models.DateTimeField(null=True)
    e_date = models.DateTimeField(null=True)
    points = models.IntegerField(default=100)
    solution = models.CharField(max_length=64)
    hint = models.CharField(max_length=512, null=True)
    tags = models.CharField(max_length=256, null=True)
    location = models.CharField(max_length=64, null=True)
    url_slug = models.SlugField(max_length=64, default="default-slug")

class Team(models.Model):
    """
    Stores name and password hash for a Team, optionally the URL to a logo image

        Fields:
            name    (str):      Name for the team
            hash    (str):      Password hash for authenticating solves/invites
            avatar  (URL):      Link to avatar image, optional
            points  (int):      Computed value that generates current score
    """
    name = models.CharField(max_length=26)
    hash = models.CharField(max_length=64)
    avatar = models.URLField(max_length=200, null=True)
    
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
    uname = models.CharField(max_length=26)
    is_owner = models.BooleanField(default=False)
    hash = models.CharField(max_length=64, null=True)
    avatar = models.URLField(max_length=200, null=True)
    email = models.EmailField(max_length=256, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

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
    event = models.ForeignKey(Event)
    index = models.IntegerField(null=True)
    s_time = models.DateTimeField(null=True)
    team = models.ForeignKey(Team, null=True)
    solved = models.BooleanField(default=False)
    member = models.ForeignKey(Member, null=True)
    s_member = models.ForeignKey(Member, null=True)
    found = models.BooleanField(default=False, null=True)
