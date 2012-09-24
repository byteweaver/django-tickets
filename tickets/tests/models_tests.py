from django.test import TestCase

from tickets.tests.factories import UserFactory, TicketFactory, TicketCommentFactory


class TicketTestCase(TestCase):
    def test_model(self):
        obj = TicketFactory()
        self.assertTrue(obj.pk)

    def test_is_closed(self):
        obj = TicketFactory()
        self.assertFalse(obj.is_closed())
        obj.status = 4
        self.assertTrue(obj.is_closed())

class TicketCommentTestCase(TestCase):
    def test_model(self):
        obj = TicketCommentFactory()
        self.assertTrue(obj.pk)

