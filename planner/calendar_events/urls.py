from django.urls import path

from .views import day_events_info, event_info, index_calendar

app_name = "calendar"


urlpatterns = [
    path("", index_calendar, name="index"),
    path("<int:event_id>/", event_info, name="event"),
    path("<str:date>/", day_events_info, name="day_events"),
]
