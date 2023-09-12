from django.contrib import admin

from links.models import Link


# Register your models here.

class LinkAdmin(admin.ModelAdmin): pass
admin.site.register(Link)


class VoteAdmin(admin.ModelAdmin): pass
