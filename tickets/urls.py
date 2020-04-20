from django.urls import path
from django.contrib.auth.decorators import login_required

from tickets.views import MyTicketListView, MyTicketDetailView, TicketCreateView


urlpatterns = [
    path('my/', login_required(MyTicketListView.as_view()), name='list'),
    path('my/<int:pk>/', login_required(MyTicketDetailView.as_view()), name='detail'),
    path('create/', login_required(TicketCreateView.as_view()), name='create'),
]
