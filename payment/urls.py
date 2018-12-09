from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^process/$', views.payment_process, name='process'),
    url(r'^done/$', views.payment_done, name='done'),
    url(r'^canceled/$', views.payment_canceled, name='canceled'),
]
#url.py is needed for django to know what url directs to which module/function/class