from django.shortcuts import render

from django.views.generic import TemplateView, \
      ListView, DetailView, CreateView

from .models import Event

class HomePageView(TemplateView):
    template_name = "home.html"
    
class EventListView(ListView):
    model = Event  
    template_name = "event_list.html"
    context_object_name = "event_list"

class EventDetailView(DetailView):
    model = Event
    template_name = "event_detail.html"
    context_object_name = "event"

class MyEventListView(ListView):
    model = Event  
    template_name = "event_list.html"
    context_object_name = "event_list"

    def get_queyset(self):
        qs = super().get_queryset()
        return qs.filter(creator=self.request.user)

class EventCreateView(CreateView):
    model = Event
    template_name = "event_create.html"
    fields = ['name', 'descriptipn', 'max_slots',
           'date_from', 'date_to', 'time_from', 'time_to', 
           'venue']
        
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


    