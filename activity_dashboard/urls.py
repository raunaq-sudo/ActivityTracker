from django.urls import path, include
from .views import EditorChartView
urlpatterns = [
    path('', EditorChartView.as_view()),
]
