from django.contrib.auth.models import User
import factory

from tickets.models import Ticket, TicketComment


class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = User

    username = factory.Sequence(lambda n: "User %s" % n)

class TicketFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Ticket

    creator = factory.LazyAttribute(lambda a: UserFactory())

class TicketCommentFactory(factory.DjangoModelFactory):
    FACTORY_FOR = TicketComment

    ticket = factory.LazyAttribute(lambda a: TicketFactory())
    author = factory.LazyAttribute(lambda a: UserFactory())

