from django.urls import path
from api.views import OsdView

urlpatterns = [
    path('', OsdView.as_view()),
]