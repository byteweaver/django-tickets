from django.views.generic import ListView, DetailView, CreateView
from django.core.urlresolvers import reverse

from forms import TicketCreateForm
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

class TicketCreateView(CreateView):
    form_class = TicketCreateForm
    template_name = 'tickets/ticket_create.html'

    def form_valid(self, form):
        ticket = form.instance
        ticket.creator = self.request.user
        ticket.save()
        self.success_url = reverse('tickets:detail', args=[ticket.id])
        return super(TicketCreateView, self).form_valid(form)
