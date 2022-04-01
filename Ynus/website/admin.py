from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Company)
admin.site.register(Discipline)
admin.site.register(Direction)
admin.site.register(DisciplineVote)
admin.site.register(VoteCompany)
