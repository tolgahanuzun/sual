" Admin Page "

from django.contrib import admin
from uptopic.models import Topic, Topic_Questions, Vote_Answer

admin.site.register(Topic)
admin.site.register(Topic_Questions)
admin.site.register(Vote_Answer)
