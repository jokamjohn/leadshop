from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^signup/$", views.MerchantRegistration.as_view(), name='merchant_signup'),
    url(r"^activate/(?P<uid>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$",
        views.ActivateUser.as_view(), name='activate'),
]
