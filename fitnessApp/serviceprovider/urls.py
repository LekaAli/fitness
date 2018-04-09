from django.conf.urls import url
from . import views

app_name = 'serviceprovider'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^add/$',views.add_service_provider,name='add'),
    url(r'^(?P<pk>[0-9]+)/detail/$',views.DetailInstitutionView.as_view(),name='detail'),
    url(r'^(?P<pk>[0-9]+)/view/$',views.RetrieveServiceProviderView.as_view(),name='view'),
    url(r'^(?P<pk>[0-9]+)/edit/$',views.EditServiceProviderView.as_view(),name='edit'),
    url(r'^(?P<service_provider_id>[0-9]+)/update/$',views.update_service_provider,name='update'),
    url(r'^(?P<service_provider_id>[0-9]+)/delete/$',views.delete_service_provider,name='delete'),
]