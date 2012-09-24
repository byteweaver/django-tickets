from django.contrib.auth.models import User
import factory

from tickets.models import Ticket, TicketComment


class UserFactory(factory.Factory):
    FACTORY_FOR = User

    username = factory.Sequence(lambda n: "User %s" % n)

class TicketFactory(factory.Factory):
    FACTORY_FOR = Ticket
    
    creator = factory.LazyAttribute(lambda a: UserFactory())

class TicketCommentFactory(factory.Factory):
    FACTORY_FOR = TicketComment

    ticket = factory.LazyAttribute(lambda a: TicketFactory())
    author = factory.LazyAttribute(lambda a: UserFactory())

