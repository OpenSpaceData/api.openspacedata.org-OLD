from django.urls import path
from api.views import ApiView

urlpatterns = [
    path('api/', ApiView.as_view()),
]