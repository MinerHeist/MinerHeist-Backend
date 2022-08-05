from django.contrib import admin
from .models import Puzzle, Team, Member, Solve

admin.site.register(Puzzle)
admin.site.register(Team)
admin.site.register(Member)
admin.site.register(Solve)