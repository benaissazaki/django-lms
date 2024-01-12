from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Session, Semester, NewsAndEvents, ActivityLog


admin.site.register(Semester)
admin.site.register(Session)
admin.site.register(NewsAndEvents)
admin.site.register(ActivityLog)
