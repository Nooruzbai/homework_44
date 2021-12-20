from django.urls import path, include

from bulls_and_cows.views import index_view, history_view


urlpatterns = [
    path('', index_view),
    path('bulls_and_cows/', history_view)
]
