from django.contrib import admin
from .models import *

# Models registration
# This gives access to data in admin page
admin.site.register(Company)
admin.site.register(Discipline)
admin.site.register(Direction)
admin.site.register(Vote)
