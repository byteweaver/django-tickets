from django.test import TestCase

from tickets.tests.factories import UserFactory, TicketFactory, TicketCommentFactory
from tickets.forms import TicketCreateForm, TicketCommentCreateForm


class TicketCreateFormTestCase(TestCase):
    def test_emtpy_form(self):
        form = TicketCreateForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'subject': ['This field is required.'],
            'description': ['This field is required.']
        })

class TicketCommentCreateFormTestCase(TestCase):
    def test_init(self):
        form = TicketCommentCreateForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'comment': ['This field is required.']
        })
