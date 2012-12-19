from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from views import MyTicketListView

urlpatterns = patterns('',
    url(r'^my/$', login_required(MyTicketListView.as_view()), name='list'),
)
