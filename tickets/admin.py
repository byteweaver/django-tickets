from django.contrib import admin

from models import Ticket, TicketComment


class TicketCommentInline(admin.StackedInline):
    model = TicketComment
    extra = 1
    raw_id_fields = ['author']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
        return super(TicketCommentInline, self).formfield_for_foreignkey(db_field, request, **kwargs)


class TicketAdmin(admin.ModelAdmin):
    list_display = ['date', 'status', 'subject', 'creator', 'assignee', 'latest_activity', 'is_answered']
    list_filter = ['status', 'date']
    search_fields = ['subject', 'description', 'creator__username', 'creator__email']
    model = Ticket
    raw_id_fields = ['creator', 'assignee']
    inlines = [TicketCommentInline, ]


admin.site.register(Ticket, TicketAdmin)
