from django.urls import path

from core.api.views import PitcherStats, HitterStats, Scheduler

urlpatterns = [
    path("pitcher-stat", PitcherStats.as_view()),
    path("hitter-stat", HitterStats.as_view()),
    path("scheduler/<str:name>&<str:period>&<str:period2>", Scheduler.as_view()),
]
