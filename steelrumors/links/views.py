from django.shortcuts import render
from django.views.generic import ListView

from links.models import Link


# Create your views here.
class LinkListView(ListView):
    model = Link

    queryset = Link.with_votes.all()
    paginate_by = 3

    template_name = 'link_list.html'

