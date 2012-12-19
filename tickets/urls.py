from django.conf.urls import patterns, url

from views import MyTicketListView

urlpatterns = patterns('',
    url(r'^my/$', MyTicketListView.as_view(), name='list'),
)
