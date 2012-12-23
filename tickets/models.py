from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from tickets import settings


class Ticket(models.Model):
    creator = models.ForeignKey(User, verbose_name=_("Creator"), related_name='tickets')
    date = models.DateTimeField(_("Date"), auto_now_add=True)
    last_update = models.DateTimeField(_("Date"), auto_now=True)
    subject = models.CharField(_("Subject"), max_length=255)
    description = models.TextField(_("Description"), help_text=_("A detailed description of your problem."))
    assignee = models.ForeignKey(User, verbose_name=_("Assignee"), related_name="assigned_tickets", blank=True, null=True)
    status = models.SmallIntegerField(_("Status"), choices=settings.STATUS_CHOICES, default=0)

    class meta:
        verbose_name = _("Ticket")
        verbose_name_plural = _("Tickets")
        ordering = ['date']

    def get_comments_count(self):
        return self.comments.count()

    def __unicode__(self):
        return "%s# %s" % (self.id, self.subject)

    def is_closed(self):
        return self.status in settings.CLOSED_STATUSES

class TicketComment(models.Model):
    ticket = models.ForeignKey(Ticket, verbose_name=_("Ticket"), related_name='comments')
    date = models.DateTimeField(auto_now_add=True, verbose_name=_("Date"), editable=False)
    author = models.ForeignKey(User, verbose_name=_("Author"))
    comment = models.TextField(_("Comment"))

    class Meta:
       verbose_name = _("Ticket comment")
       verbose_name_plural = _("Ticket comments")
       ordering = ['date']

    def __unicode__(self):
        return "Comment on " + unicode(self.ticket)

