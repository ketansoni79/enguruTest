from django.conf.urls import url
from .views import TaskView, UserTaskView

urlpatterns = [
    url(r'^$', UserTaskView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', TaskView.as_view())
]