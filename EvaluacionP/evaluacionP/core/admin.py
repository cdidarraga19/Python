from django.contrib import admin
from .models import Team, GamePosition, Player, Nacionality, TechincalDirector

admin.site.register(Team)
admin.site.register(GamePosition)  
admin.site.register(Player)
admin.site.register(Nacionality)
admin.site.register(TechincalDirector)