from django.urls import path
from .views import CreateResultView, ResultView, SearchView

urlpatterns = [
    path('result', ResultView.as_view()),
    path('create-result', CreateResultView.as_view()),
    path('search', SearchView.as_view())
]
