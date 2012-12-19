from django.views.generic import ListView, DetailView

from models import Ticket


class MyTicketListView(ListView):
    model = Ticket
    template_name = 'tickets/ticket_mylist.html'

    def get_queryset(self):
        return Ticket.objects.filter(creator=self.request.user)

class MyTicketDetailView(DetailView):
    model = Ticket
    template_name = 'tickets/ticket_mydetail.html'

    def get_queryset(self):
        return Ticket.objects.filter(creator=self.request.user)
