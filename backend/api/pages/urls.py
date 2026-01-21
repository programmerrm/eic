from django.urls import path
from api.pages.views.pages import PageViewSet

urlpatterns = [
    path("list/", PageViewSet.as_view()),
    path("<slug:slug>/", PageViewSet.as_view()),
]
