from django.contrib import admin
from .models import Type, Song
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.register(Type)
admin.site.register(Song)