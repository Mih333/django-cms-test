from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from projects import views

urlpatterns = [
    url(r'^$', views.MainView.as_view()),
    url(r'^save-options/$', views.SaveOption.as_view())
]
