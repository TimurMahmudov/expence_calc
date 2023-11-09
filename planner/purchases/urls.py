from django.urls import path

from .views import GeneralInfoView

app_name = "purchases"


urlpatterns = [
    path("", GeneralInfoView.as_view(), name="general"),
]
