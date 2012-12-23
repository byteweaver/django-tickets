from django.contrib import admin

from models import Ticket, TicketComment


class TicketCommentInline(admin.StackedInline):
    model = TicketComment
    extra = 1


class TicketAdmin(admin.ModelAdmin):
    model = Ticket
    inlines = [TicketCommentInline,]


admin.site.register(Ticket, TicketAdmin)
