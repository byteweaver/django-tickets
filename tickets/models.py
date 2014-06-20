from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from tickets.settings import STATUS_CHOICES, CLOSED_STATUSES


class Ticket(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Creator"), related_name='tickets')
    date = models.DateTimeField(_("Date"), auto_now_add=True)
    last_update = models.DateTimeField(_("Date"), auto_now=True)
    subject = models.CharField(_("Subject"), max_length=255)
    description = models.TextField(_("Description"), help_text=_("A detailed description of your problem."))
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Assignee"), related_name="assigned_tickets", blank=True, null=True)
    status = models.SmallIntegerField(_("Status"), choices=STATUS_CHOICES, default=0)

    class meta:
        verbose_name = _("Ticket")
        verbose_name_plural = _("Tickets")
        ordering = ['date']

    def get_comments_count(self):
        return self.comments.count()

    def get_latest_comment(self):
        return self.comments.latest('date')

    def __unicode__(self):
        return "%s# %s" % (self.id, self.subject)

    def is_closed(self):
        return self.status in CLOSED_STATUSES

    def is_answered(self):
        try:
            latest = self.get_latest_comment()
        except TicketComment.DoesNotExist:
            return False
        return latest.author != self.creator
    is_answered.boolean = True
    is_answered.short_description = _("Is answered")


class TicketComment(models.Model):
    ticket = models.ForeignKey(Ticket, verbose_name=_("Ticket"), related_name='comments')
    date = models.DateTimeField(auto_now_add=True, verbose_name=_("Date"))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Author"))
    comment = models.TextField(_("Comment"))

    class Meta:
        verbose_name = _("Ticket comment")
        verbose_name_plural = _("Ticket comments")
        ordering = ['date']

    def __unicode__(self):
        return "Comment on " + unicode(self.ticket)
