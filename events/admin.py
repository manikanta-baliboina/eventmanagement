from django.contrib import admin
from .models import Event, Participant


# 👇 Shows participants inside Event page
class ParticipantInline(admin.TabularInline):
    model = Participant
    extra = 0
    readonly_fields = ('name', 'email', 'phone')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'capacity', 'total_participants')
    search_fields = ('title', 'location')
    list_filter = ('date',)
    inlines = [ParticipantInline]

    def total_participants(self, obj):
        return obj.participants.count()

    total_participants.short_description = "Registered Users"


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'event')
    search_fields = ('name', 'email')
    list_filter = ('event',)
