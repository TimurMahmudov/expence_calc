from django.urls import path

from .views import CategoryInfoView, GeneralInfoView, create_expenses

app_name = "purchases"


urlpatterns = [
    path("", GeneralInfoView.as_view(), name="index"),
    path("add_posts/", create_expenses, name="create_posts"),
    path("<slug:slug>/", CategoryInfoView.as_view(), name="category"),
]
