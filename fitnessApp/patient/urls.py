from django.conf.urls import url
from . import views


app_name = 'patient'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^add/$',views.add_patient,name='add'),
    url(r'^(?P<pk>[0-9]+)/detail/$',views.DetailView.as_view(),name='detail'),
    url(r'^(?P<pk>[0-9]+)/view/$',views.DetailView.as_view(),name='view'),
    url(r'(?P<pk>[0-9]+)/edit/$',views.UpdateView.as_view(),name='edit'),
    url(r'(?P<patient_id>[0-9]+)/update/$',views.update_patient,name='update'),
    url(r'(?P<pk>[0-9]+)/deleteview/$',views.UpdateView.as_view(),name='deleteView'),
    url(r'(?P<patient_id>[0-9]+)/delete/$',views.delete_patient,name='delete'),
    url(r'(?P<patient_id>[0-9]+)/delete_view/$',views.delete_view_patient,name='delete_view'),
]
