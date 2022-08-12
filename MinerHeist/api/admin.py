from django.contrib import admin
from .models import Event, Team, Member, Assignment

admin.site.register(Event)
admin.site.register(Team)
admin.site.register(Member)
admin.site.register(Assignment)