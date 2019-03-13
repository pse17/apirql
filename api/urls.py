from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView

urlpatterns = [
    path('users', CreateView.as_view(), name='create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
