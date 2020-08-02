#!/usr/bin/env python3

from django.conf.urls import url
from rest.app.profile.views import UserProfileView


urlpatterns = [
    url(r'^profile', UserProfileView.as_view()),
    ]
