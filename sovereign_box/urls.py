from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^contact', views.ContactUsView.as_view(), name='tags'),
    url(r'^tags', views.TagCoinView.as_view(), name='tags'),
    url(r'^coins', views.CoinsListView.as_view(), name='coins'),
    url(r'^user/create', views.CreateUserView.as_view(), name='create_user'),
    url(r'^user/token', views.CreateTokenView.as_view(), name='create_token'),
]
