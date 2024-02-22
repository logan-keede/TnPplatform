from django.contrib import admin
from Announcement.models import Announcement

from .models import Announcement


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')
    search_fields = ('title', 'content')
    list_filter = ('date_posted',)

# Register your models here.

    list_filter = ('date_posted',)
