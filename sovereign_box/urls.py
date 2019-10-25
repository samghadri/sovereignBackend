from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^coins', views.CoinsListView.as_view(), name='coins'),
]
