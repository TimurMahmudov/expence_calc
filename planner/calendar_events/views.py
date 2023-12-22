import datetime
from typing import Dict, List
import locale

from django.shortcuts import get_object_or_404, render

from .models import Event

FORMAT_DAY = "%A %d %B %Y"

weekDaysMapping = ["Понедельник", "Вторник", "Среда",
                   "Четверг", "Пятница", "Суббота",
                   "Воскресенье"]


def get_range_date():
    start_day = datetime.date.today()
    week_later = start_day + datetime.timedelta(days=7)
    two_week_later = start_day + datetime.timedelta(days=14)
    month_later = start_day + datetime.timedelta(days=30)
    return start_day, week_later, two_week_later, month_later


def sorting_events(events: List[Event], last_query: Dict):
    events_values = events.values()
    for event_dict in events_values:
        date = event_dict["time"].date()
        if date not in last_query:
            last_query[date] = [{
                "title": event_dict["title"],
                "id": event_dict["id"],
                "time": event_dict["time"].time
            }]
        else:
            last_query[date].append({
                "title": event_dict["title"],
                "id": event_dict["id"],
                "time": event_dict["time"].time
            })
    return last_query


def index_calendar(request):
    start, week_1, two_week, month = get_range_date()
    template_name = "calendar/calendar_index.html"
    events = Event.objects.filter(time__range=(start, week_1))
    last_query = {}
    sorting_events(events, last_query)
    context = {
        "week": last_query,
        #"two_week": Event.objects.filter(time__range=(start, two_week)),
        #"month": Event.objects.filter(time__range=(start, month))
    }
    return render(request, template_name, context)


def event_info(request, event_id):
    context = {
        "event": get_object_or_404(Event, pk=event_id)
    }
    template_name = "calendar/event_info.html"
    return render(request, template_name, context)


def day_events_info(request, date):
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    events = Event.objects.filter(time__date=date)
    template_name = "calendar/day_info.html"
    context = {
        "events": events,
        "date": (date.date(), weekDaysMapping[date.weekday()])
    }
    return render(request, template_name, context)
