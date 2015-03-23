from django import forms

from tickets.models import Ticket, TicketComment


class TicketCreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('subject', 'description')


class TicketCommentCreateForm(forms.ModelForm):
    class Meta:
        model = TicketComment
        fields = ('comment',)
