from django.urls import path

from .views import HomePageView, EventListView, \
     EventDetailView, MyEventListView, EventCreateView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("events/", EventListView.as_view(),
       name="event_list"),

    path("events/my/", MyEventListView.as_view(),
       name="myevent_list"),

    path("events/new/", EventCreateView.as_view(),
       name="event_create"),

    path("event/<int:pk>/", EventDetailView.as_view(),
       name="event_detail")
]