from django.views.generic import ListView, DetailView, CreateView
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _

from forms import TicketCreateForm, TicketCommentCreateForm
from models import Ticket


class MyTicketListView(ListView):
    model = Ticket
    template_name = 'tickets/ticket_mylist.html'

    def get_queryset(self):
        return Ticket.objects.filter(creator=self.request.user)

class MyTicketDetailView(DetailView):
    model = Ticket
    template_name = 'tickets/ticket_mydetail.html'
    form = TicketCommentCreateForm()

    def get_context_data(self, **kwargs):
        context = super(MyTicketDetailView, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        self.form = TicketCommentCreateForm(request.POST)
        if self.form.is_valid():
            self.form_valid(self.form)
            return HttpResponseRedirect(reverse('tickets:detail', args=[self.kwargs['pk']]))
        return super(MyTicketDetailView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.instance
        comment.author = self.request.user
        comment.ticket = Ticket.objects.get(id=self.kwargs['pk'])
        comment.save()
        messages.success(self.request, _("Ticket comment created."))

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
        messages.success(self.request, _("Ticket created."))
        return super(TicketCreateView, self).form_valid(form)
