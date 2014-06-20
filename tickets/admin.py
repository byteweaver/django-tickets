from django.contrib import admin

from models import Ticket, TicketComment


class TicketCommentInline(admin.StackedInline):
    model = TicketComment
    extra = 1
    raw_id_fields = ['author']


class TicketAdmin(admin.ModelAdmin):
    model = Ticket
    raw_id_fields = ['creator', 'assignee']
    inlines = [TicketCommentInline, ]


admin.site.register(Ticket, TicketAdmin)
