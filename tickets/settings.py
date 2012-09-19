from django.conf import settings
from django.utils.translation import ugettext_lazy as _


# List of available status options
STATUS_CHOICES = getattr(settings, 'TICKETS_STATUS_CHOICES', (
    (0, _("New")),
    (1, _("Feedback")),
    (3, _("In Progress")),
    (4, _("Resolved")),
    (5, _("Closed")),
    ))

# List of statuses that define a ticket as finally closed
CLOSED_STATUSES = getattr(settings, 'TICKETS_CLOSED_STATUSES', (4,5))

