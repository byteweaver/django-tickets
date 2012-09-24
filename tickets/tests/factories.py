from django.contrib.auth.models import User
import factory

from tickets.models import Ticket


class UserFactory(factory.Factory):
    FACTORY_FOR = User

class TicketFactory(factory.Factory):
    FACTORY_FOR = Ticket
    
    creator = factory.LazyAttribute(lambda a: UserFactory())
