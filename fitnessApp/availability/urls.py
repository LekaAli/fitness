from django.conf.urls import url
from . import views

app_name = 'availability'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^add/$',views.AddAvailabilityView.as_view(),name='add'),
    url(r'^(?P<availability_id>[0-9]+)/edit/$',views.edit_availability,name='edit'),
    url(r'^(?P<pk>[0-9]+)/detail/$',views.DetailAvailabilityView.as_view(),name='detail'),
    url(r'^(?P<availability_id>[0-9]+)/update/$',views.update_availability,name='update'),
    url(r'(?P<serviceprovider_id>[0-9]+)/delete/$',views.delete_availability,name='delete'),
    url(r'(?P<serviceprovider_id>[0-9]+)/delete/$',views.check_availability,name='check'),
]